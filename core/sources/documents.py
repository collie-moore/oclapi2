from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from pydash import get

from core.sources.models import Source


@registry.register_document
class SourceDocument(Document):
    class Index:
        name = 'sources'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    locale = fields.ListField(fields.TextField())
    last_update = fields.DateField(attr='updated_at')
    sourceType = fields.TextField(attr='source_type')
    owner = fields.TextField(attr='parent_resource')
    owner_type = fields.TextField(attr='parent_resource_type')
    public_can_view = fields.TextField(attr='public_can_view')
    customValidationSchema = fields.TextField(attr='custom_validation_schema')

    class Django:
        model = Source
        fields = [
            'name',
            'full_name',
            'is_active'
        ]

    @staticmethod
    def prepare_locale(instance):
        return get(instance.supported_locales, [])
