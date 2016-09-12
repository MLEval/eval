from flask import request, abort
from decimal import Decimal

from e.model.model import Model
from e.model.prediction import Prediction
from e.utils import serialize_response


@serialize_response
def add_model_prediction(mid):
    model = Model.objects.get_or_404(id=mid)

    # request.form is immutable :(
    # TODO(rossem): if they don't pass an identifier, we should generate one
    # and return it. Maybe we can just return the prediciction token.
    identifier = request.form['identifier']
    probability = request.form['probability']
    threshold = request.form.get('threshold')
    klass = request.form.get('class')
    value = request.form.get('value')

    if Prediction.objects(mid=mid, identifier=identifier):
        abort(400)

    if klass and klass not in model.classes:
        abort(400)

    if value and value not in model.classes:
        abort(400)

    # Since we want to store probability/threshold pertaining only to the 
    # positive class for uniformity of data, we must flip the values if the
    # user sent a request pertaining to the negative class. If `class` is not
    # passed, assume that it is the positive one.
    # TODO(rossem): allow them to pass `positive/negative` instead of the name
    if klass == model.negative_class:
        probability = 1 - Decimal(probability)
        if threshold:
            threshold = 1 - Decimal(threshold)

    if threshold and value:
        # Compare strictly as it is not clear how the user intends to
        # proceed when probability == threshold.
        if probability > threshold and value == model.negative_class or \
           probability < threshold and value == model.positive_class:
            abort(400)

    return Prediction(**{
        'mid': mid,
        'identifier': identifier,
        'probability': probability,
        'threshold': threshold,
        'value': value
    }).save()


@serialize_response
def get_model_predictions(mid):
    return Prediction.objects(mid=mid)
