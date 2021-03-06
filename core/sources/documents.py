from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from pydash import get

from core.sources.models import Source


@registry.register_document
class SourceDocument(Document):
    class Index:
        name = 'sources'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    locale = fields.ListField(fields.KeywordField())
    last_update = fields.DateField(attr='updated_at')
    owner = fields.KeywordField(attr='parent_resource', normalizer='lowercase')
    owner_type = fields.KeywordField(attr='parent_resource_type')
    public_can_view = fields.TextField(attr='public_can_view')
    source_type = fields.KeywordField(attr='source_type', normalizer='lowercase')
    is_active = fields.KeywordField(attr='is_active')
    version = fields.KeywordField(attr='version')
    name = fields.KeywordField(attr='name', normalizer='lowercase')
    canonical_url = fields.KeywordField(attr='canonical_url', normalizer='lowercase')
    mnemonic = fields.KeywordField(attr='mnemonic', normalizer='lowercase')
    extras = fields.ObjectField()

    class Django:
        model = Source
        fields = [
            'full_name',
            'custom_validation_schema',
        ]

    @staticmethod
    def prepare_locale(instance):
        return get(instance.supported_locales, [])

    @staticmethod
    def prepare_extras(instance):
        return instance.extras or {}
