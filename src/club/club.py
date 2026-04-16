"""

Authors
-------
Alberto Zancanaro <alberto.zancanaro@uni.lu>

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import typer

from typing import Optional
from typing_extensions import Annotated

from . import support_function, caveman_compress_mlm, caveman_compress_nlp
from .support_enum import language, mode

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Default commands (without specifying llm/mlm/nlp)

def club_compress(
    text       : Annotated[Optional[str]     , typer.Argument(help = "The text you want to compress.")] = None,
    input_file : Annotated[Optional[str]     , typer.Option("--input"   , "-i", help = "The input file with the text you want to compress. If passed together with text, the text will take precedence and a copy of the text will be saved to the input file (backup). If a file already exists at the input file path, it will be overwritten without warning.")] = None,
    output_file: Annotated[Optional[str]     , typer.Option("--output"  , "-o", help = "The output file with the text you want to compress")] = None,
    language   : Annotated[Optional[language], typer.Option("--language", "-l", help = "language code (en, es, de, fr, etc.)")] = language.en,
    verbose    : Annotated[bool              , typer.Option("--verbose" , "-v", help = "Enable verbose output")] = False,
) :
    """
    If you do not specify llm/mlm/nlp when you call the command, it will default to the NLP-based compression method (i.e. if you call `club compress` is equivalent to `club nlp compress`).
    """

    club_nlp(
        mode = "compress",
        text = text,
        input_file = input_file,
        output_file = output_file,
        language = language,
        verbose = verbose
    )

def club_decompress(
    text       : Annotated[Optional[str]     , typer.Argument(help = "The text you want to decompress.")] = None,
    input_file : Annotated[Optional[str]     , typer.Option("--input"   , "-i", help = "The input file with the text you want to decompress. If passed together with text, the text will take precedence and a copy of the text will be saved to the input file (backup). If a file already exists at the input file path, it will be overwritten without warning.")] = None,
    output_file: Annotated[Optional[str]     , typer.Option("--output"  , "-o", help = "The output file with the text you want to decompress")] = None,
    language   : Annotated[Optional[language], typer.Option("--language", "-l", help = "language code (en, es, de, fr, etc.)")] = language.en,
    verbose    : Annotated[bool              , typer.Option("--verbose" , "-v", help = "Enable verbose output")] = False,
) :
    """
    If you do not specify llm/mlm/nlp when you call the command, it will default to the NLP-based decompression method (i.e. if you call `club decompress` is equivalent to `club nlp decompress`).
    """

    club_nlp(
        mode = "decompress",
        text = text,
        input_file = input_file,
        output_file = output_file,
        language = language,
        verbose = verbose
    )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def club_llm(
    mode   : Annotated[mode         , typer.Argument(help = "The type or process you want to apply. Possible value are compress or decompress")],
    text   : Annotated[Optional[str], typer.Argument(help = "The text you want to process.")] = None,
    input_file     : Annotated[Optional[str]  , typer.Option("--input"   , "-i", help = "The input file with the text you want to compress. If passed together with text, the text will take precedence and a copy of the text will be saved to the input file (backup). If a file already exists at the input file path, it will be overwritten without warning.")] = None,
    output_file    : Annotated[Optional[str]  , typer.Option("--output"  , "-o", help = "The output file with the text you want to compress")] = None,
) :
    """
    TODO
    """

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def club_mlm(
    mode           : Annotated[mode         , typer.Argument(help = "The type or process you want to apply. Possible value are compress or decompress")],
    text           : Annotated[Optional[str], typer.Argument(help = "The text you want to process.")] = None,
    input_file     : Annotated[Optional[str]  , typer.Option("--input"   , "-i", help = "The input file with the text you want to compress. If passed together with text, the text will take precedence and a copy of the text will be saved to the input file (backup). If a file already exists at the input file path, it will be overwritten without warning.")] = None,
    output_file    : Annotated[Optional[str]  , typer.Option("--output"  , "-o", help = "The output file with the text you want to compress")] = None,
    verbose        : Annotated[bool           , typer.Option("--verbose" , "-v", help = "Enable verbose output")] = False,
    prob_threshold : Annotated[Optional[float], typer.Option("--prob-threshold", "-p", help = "probability threshold: remove words with P >= this value (default: 1e-5)")] = 1e-5,
    no_adjacent    : Annotated[bool           , typer.Option("--no-adjacent"   , help = "Never remove two adjacent words; if both exceed threshold, remove only the highest probability one")] = False,
    no_protect_ner : Annotated[bool           , typer.Option("--no-protect-ner", help = "Disable NER protection (by default, named entities like PERSON, ORG, GPE, DATE are preserved)")] = False,
) :
    """
    MLM-based caveman compression using RoBERTa. Removes highly predictable tokens based on masked language model probabilities. No LLM API required - uses local RoBERTa model for deterministic compression.

    Probability thresholds:
      P >= 1e-3:  Conservative (16% reduction, 98% accuracy)
      P >= 1e-4:  Moderate (19% reduction, 97% accuracy)
      P >= 1e-5:  Balanced (32% reduction, 92% accuracy) [DEFAULT]
      P >= 1e-6:  Aggressive (54% reduction, 83% accuracy)
    """

    # Get input text
    input_text = support_function.check_and_get_input_text(text, input_file)

    # (OPTIONAL) Verbose preamble and start
    if verbose :
        support_function.verbose_preamble_nlp(mode, language)
        support_function.verbose_start(mode, input_text)

    # Process text
    if mode == "compress" :
        output_text = caveman_compress_mlm.compress_text(input_text, prob_threshold, no_adjacent, no_protect_ner)
    elif mode == "decompress" :
        output_text = caveman_compress_mlm.decompress_text(text)

    # (OPTIONAL) Verbose end
    if verbose : support_function.verbose_end(mode, input_text, output_text)

    # If not output file is provided, print the output text to the console. Otherwise, save the output text to the output file.
    if output_file is not None : support_function.save_output_text(output_text, output_file, verbose)
    else : print(f"\nOutput text:\n{output_text}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def club_nlp(
    mode        : Annotated[mode         , typer.Argument(help = "The type or process you want to apply. Possible value are compress or decompress")],
    text        : Annotated[Optional[str], typer.Argument(help = "The text you want to process.")] = None,
    input_file  : Annotated[Optional[str]     , typer.Option("--input"   , "-i", help = "The input file with the text you want to compress. If passed together with text, the text will take precedence and a copy of the text will be saved to the input file (backup). If a file already exists at the input file path, it will be overwritten without warning.")] = None,
    output_file : Annotated[Optional[str]     , typer.Option("--output"  , "-o", help = "The output file with the text you want to compress")] = None,
    language    : Annotated[Optional[language], typer.Option("--language", "-l", help = "language code (en, es, de, fr, etc.)")] = language.en,
    verbose     : Annotated[bool              , typer.Option("--verbose" , "-v", help = "Enable verbose output")] = False,
) :
    """
    NLP-based caveman compression without LLM. Fast, free, deterministic - uses stop word removal and grammar stripping. Supports multiple languages via spaCy.
    """
    
    # Get input text
    input_text = support_function.check_and_get_input_text(text, input_file)

    # (OPTIONAL) Verbose preamble and start
    if verbose :
        support_function.verbose_preamble_nlp(mode, language)
        support_function.verbose_start(mode, input_text)

    # Process text
    if mode == "compress" :
        output_text = caveman_compress_nlp.compress_text(input_text, language)
    elif mode == "decompress" :
        output_text = caveman_compress_nlp.decompress_text(text)

    # (OPTIONAL) Verbose end
    if verbose : support_function.verbose_end(mode, input_text, output_text)

    # If not output file is provided, print the output text to the console. Otherwise, save the output text to the output file.
    if output_file is not None : support_function.save_output_text(output_text, output_file, verbose)
    else : print(f"\nOutput text:\n{output_text}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

