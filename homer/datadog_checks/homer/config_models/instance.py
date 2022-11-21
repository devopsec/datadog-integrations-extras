# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional, Sequence

from pydantic import BaseModel, Field, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class HomerConfigDb(BaseModel):
    class Config:
        allow_mutation = False

    host: Optional[str]
    name: Optional[str]
    pass_: Optional[str] = Field(None, alias='pass')
    port: Optional[int]
    user: Optional[str]


class HomerDataDb(BaseModel):
    class Config:
        allow_mutation = False

    host: Optional[str]
    name: Optional[str]
    pass_: Optional[str] = Field(None, alias='pass')
    port: Optional[int]
    user: Optional[str]


class MetricPatterns(BaseModel):
    class Config:
        allow_mutation = False

    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    homer_config_db: HomerConfigDb
    homer_data_db: HomerDataDb
    homer_service_checks: Sequence[str]
    metric_patterns: Optional[MetricPatterns]
    min_collection_interval: Optional[float]
    service: Optional[str]
    tags: Optional[Sequence[str]]

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
