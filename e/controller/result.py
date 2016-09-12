from flask import request, abort

from e.model.model import Model
from e.model.prediction import Prediction
from e.model.result import Result
from e.utils import serialize_response


@serialize_response
def add_model_result(mid):
    model = Model.objects.get_or_404(id=mid)
    prediction = Prediction.objects.get_or_404(
        mid=mid, identifier=request.form['identifier'])

    if Result.objects(mid=mid, identifier=request.form['identifier']):
        abort(400)

    if request.form['value'] not in model.classes:
        abort(400)

    return Result(**{
        'mid': mid,
        'pid': prediction.id,
        'identifier': request.form['identifier'],
        'value': request.form['value']
    }).save()


@serialize_response
def get_model_results(mid):
    return Result.objects(mid=mid)
