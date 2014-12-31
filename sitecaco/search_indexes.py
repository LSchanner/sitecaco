from haystack import indexes
import datetime
from .models import *

class IndexNoticia(indexes.SearchIndex, indexes.Indexable):
    title =  indexes.CharField(model_attr='title')
    text =  indexes.CharField(use_template=True, document=True)
    time = indexes.DateTimeField(model_attr='time')

    def get_model(self):
        return Noticia

class IndexaAta(indexes.SearchIndex, indexes.Indexable):
    title =  indexes.CharField(model_attr='title')
    text =  indexes.CharField(use_template=True, document=True)
    time = indexes.DateTimeField(model_attr='time')

    def get_model(self):
        return Ata

class IndexPagina(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    text =  indexes.CharField(use_template=True, document=True)

    def get_model(self):
        return Pagina


