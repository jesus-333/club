"""

Authors
-------
Alberto Zancanaro <alberto.zancanaro@uni.lu>

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Functions by wilpel

def count_tokens(text):
    """
    Estimate token count: characters / 4

    Originally developed by wilpel. Copied here because it is the same in all three scripts.
    """

    return len(text.strip()) // 4

def compute_reduction(input_text, output_text) :
    """
    Compute the percentage reduction in token count from input_text to output_text.

    Originally developed by wilpel. Copied here because it is the same in all three scripts.
    """

    orig_tokens = count_tokens(input_text)
    comp_tokens = count_tokens(output_text)
    reduction = ((orig_tokens - comp_tokens) / orig_tokens * 100) if orig_tokens > 0 else 0

    return orig_tokens, comp_tokens, reduction

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Other utility functions

def print_separator(symbol = "%", length = 40):
    """
    Print a separator line of a given symbol and length.
    """

    print("\n", symbol * length)

def check_and_get_input_text(text, input_file) :
    """

    """

    if text is None and input_file is None :
        # If neither text nor input file is provided, raise an error
        raise ValueError("Provide text or use --input for file input")
    elif text is not None and input_file is not None :
        # If both text and input file are provided, text takes the precedence and a copy of the text is saved to the input file
        # If a file already exists at the input file path, it will be overwritten without warning
        with open(input_file, "w") as f :
            f.write(text)
        input_text = text
    elif text is not None and input_file is None :
        # If only text is provided, use it as input text
        input_text = text
    elif text is None and input_file is not None :
        # If only input file is provided, read the text from the file
        if not os.path.exists(input_file) :
            raise FileNotFoundError(f"File not found: {input_file}")
        with open(input_file, "r") as f :
            input_text = f.read()

    return input_text

def save_output_text(output_text, output_file, verbose : bool = False) :
    """
    Save the output text to a file if output_file is provided.
    """

    if output_file is not None :
        with open(output_file, "w") as f :
            f.write(output_text)

    if verbose : print(f"\nOutput saved to: {output_file}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VERBOSE Functions - Preamble

def verbose_preamble_nlp(mode, language):
    """
    Print verbose preamble with the settings used for compression or decompression.
    """
    
    print_separator("%", 30)
    print(f"Mode     : {mode}")
    print(f"Language : {language}")

def verbose_preamble_mlm(mode, probability_threshold, no_adjacent, no_protect_ner):
    """
    Print verbose preamble with the settings used for compression or decompression.
    """
    
    print_separator("%", 30)
    print(f"Mode                  : {mode}")
    print(f"Probability threshold : {probability_threshold}")
    print(f"No adjacent           : {no_adjacent}")
    print(f"No protect NER        : {no_protect_ner}")


def verbose_preamble_llm() :
    """
    TODO
    """
    pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VERBOSE Functions - Start and End Computation

def verbose_start(mode, input_text) :

    if mode == "compress" :
        print_separator("%", 30)
        print("ORIGINAL TEXT:")
        print(input_text)
        print("\nCompressing...")
    elif mode == "decompress" :
        print_separator("%", 30)
        print("COMPRESSED TEXT:")
        print(input_text)
        print("\nDecompressing...")

def verbose_end(mode, input_text, output_text) :

    if mode == "compress" :
        print_separator("%", 30)
        print("CAVEMAN COMPRESSED:")
        print(output_text)

        print_separator("%", 30)
        print("STATISTICS:")
        orig_tokens, comp_tokens, reduction = compute_reduction(input_text, output_text)
        print(f"\tOriginal   : {len(input_text)} chars ≈ {orig_tokens} tokens")
        print(f"\tCompressed : {len(output_text)} chars ≈ {comp_tokens} tokens")
        print(f"\tReduction  : {reduction:.1f}%")
    elif mode == "decompress" :
        print_separator("%", 30)
        print("DECOMPRESSED:")
        print(output_text)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 
