#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Structural ambiguity resolution.

Structural ambiguities occur when a sentence admits multiple plausible
syntactic parses (PP-attachment, coordination scope, relative-clause
attachment, modifier scope). See paper §Methodology.
"""

from common import BaseAmbiguityResolver, run_cli


class StructuralResolver(BaseAmbiguityResolver):
    ambiguity_type = "structural"

    ambiguity_definition = (
        "Structural ambiguity occurs when a sentence can be parsed in more than "
        "one way, producing different meanings. Common patterns include:\n"
        "  - PP attachment: 'process data using algorithm specified in document' "
        "(does 'specified' modify 'algorithm' or 'document'?)\n"
        "  - Coordination scope: 'validate and store data in database' "
        "(does 'in database' apply to both actions?)\n"
        "  - Relative-clause attachment: 'log operations performed by users on systems'\n"
        "  - Modifier scope: 'send requests to servers using encryption'."
    )

    cot_steps = [
        "Scan the requirement for structural-ambiguity patterns "
        "(PP attachment, coordination, relative clauses, modifier scope).",
        "For each pattern, enumerate the plausible parses.",
        "Decide whether the intended parse is clear from context.",
        "If ambiguous, rewrite to make the intended attachment/scope explicit.",
        "Produce the complete fixed requirement.",
    ]

    critical_rules = [
        "Clarify all ambiguous attachments and scope relationships.",
        "Prefer minimal edits that disambiguate without changing meaning.",
        "Add words such as 'that', 'which', or repeat the noun when needed.",
        "Always output the COMPLETE requirement text.",
        "If no structural ambiguity is found, output the original text unchanged.",
    ]

    default_examples = [
        {
            "original": "The system shall process user requests using the security protocols defined in the manual.",
            "fixed":    "The system shall process user requests using the security protocols that are defined in the manual.",
        },
        {
            "original": "The application shall validate and store user data in the database using encryption.",
            "fixed":    "The application shall validate user data and store user data in the database, using encryption for both operations.",
        },
        {
            "original": "The module shall send requests to servers using encryption protocols.",
            "fixed":    "The module shall send requests to servers, where the module uses encryption protocols for sending.",
        },
    ]


if __name__ == "__main__":
    run_cli(StructuralResolver, default_csv="data/structural.csv")
