from typing import List, Dict, NamedTuple, Optional, Any

## Material and quantity data type

class MatQuant(NamedTuple):
    class Amount(NamedTuple):
        value: float
        unit: str
    amount: List[Amount]
    material: str

## Sentence-level data types

class Sentence(NamedTuple):

    class ProcedureStep(NamedTuple):
        class SentCondition(NamedTuple):
            max: float
            min: float
            tok_ids: List[int]
            values: List[float]
            unit: str
        env_ids: Optional[List[List[int]]]
        env_toks: Optional[List[str]]
        op_id: int
        op_token: str
        op_type: str
        ref_op: bool
        subject: str
        subsent: List[int]
        temp_values: Optional[SentCondition]
        time_values: Optional[SentCondition]

    all_materials: List[MatQuant]
    other_materials: List[str]
    precursors: List[MatQuant]
    target: List[str]
    procedure_graph: List[ProcedureStep]


## Paragraph-level data types

class Paragraph(NamedTuple):

    class SynthAction(NamedTuple):
        class ParaCondition(NamedTuple):
            class ParaValue(NamedTuple):
                max_value: float
                min_value: float
                values: List[float]
                unit: str
            temperature: Optional[ParaValue]
            time: Optional[ParaValue]
        conditions: ParaCondition
        string: str
        type: str

    class MorphInfo(NamedTuple):
        descriptors: List[str]
        measurements: List[str]
        morphologies: List[str]
        sizes: List[str]
        units: List[str]

    class MorphNER(NamedTuple):
        annotation: str
        end: int
        start: int
        text: str

    _id: str
    contains_recipe: bool
    contains_characterization: bool
    materials_and_quantities: Optional[MatQuant]
    morphological_information: Optional[MorphInfo]
    morphology_ner_tokens: Optional[List[MorphNER]]
    seed_mediated: Optional[bool]
    sentences: Optional[List[Sentence]]
    synth_actions: Optional[List[SynthAction]]
    text: str

## Paper-level data types

class Paper(NamedTuple):
    doi: str
    publication_year: int
    times_referenced: int
    paragraphs: List[Paragraph]
