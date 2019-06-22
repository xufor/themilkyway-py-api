from ma import ma
from models.views import ViewsModel


class ViewSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = ViewsModel
        dump_only = ('time', 'source', 'sno')
