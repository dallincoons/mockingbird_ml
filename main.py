from textgenrnn import textgenrnn

def main():
    textgen = textgenrnn(weights_path='data/word/colaboratory_weights.hdf5',
                     vocab_path='data/word/colaboratory_vocab.json',
                     config_path='data/word/colaboratory_config.json')

    textgen.generate_samples(max_gen_length=1000)
    # textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

if __name__ == '__main__':
    main()
