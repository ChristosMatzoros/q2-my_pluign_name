# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat


# A description
def stats(
    seqs: DNAFASTAFormat,
    debug: bool = False,
) -> (DNAFASTAFormat):

    if seqs:
        # Fetch taxonomy (also needed for custom databases)
        fasta_file_path = str(seqs.path)

        # Initialize an empty list to store sequences
        sequences = []

        # Open the .fasta file and read its contents line by line
        try:
            with open(fasta_file_path, "r") as fasta_file:
                sequence = ""  # Initialize an empty string for the first sequence
                for line in fasta_file:
                    # Remove leading and trailing whitespace
                    line = line.strip()

                    # Check if the line is empty (skip empty lines)
                    if not line:
                        continue

                    # Check if the line starts with '>' indicating a sequence ID
                    if line.startswith(">"):
                        # If we already have a sequence, append it to the list
                        if sequence:
                            sequences.append(sequence)

                        # Reset the sequence string for the new record
                        sequence = ""
                    else:
                        # Append the line to the sequence
                        sequence += line

                # Append the last sequence in the file to the list
                if sequence:
                    sequences.append(sequence)

        except FileNotFoundError:
            print(f"The file '{fasta_file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    else:
        return seqs

    lengths = [len(seq) for seq in sequences]

    # Compute statistics
    mean_length = sum(lengths) / len(lengths)
    median_length = sorted(lengths)[len(lengths) // 2]
    std_deviation = (sum((x - mean_length) ** 2 for x in lengths) / len(lengths)) ** 0.5

    # Format and print the statistics
    print(f"Mean Length: {mean_length:.{2}f}")
    print(f"Median Length: {median_length:.{2}f}")
    print(f"Standard Deviation: {std_deviation:.{2}f}")

    return seqs
