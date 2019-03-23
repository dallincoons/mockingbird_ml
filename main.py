from textgenrnn import textgenrnn

def main():
    # textgen = textgenrnn()
    # textgen.train_from_file('data/cleaned_tweets.csv', num_epochs=1, is_csv=True)
    # textgen.generate()

    # textgen = textgenrnn('textgenrnn_weights.hdf5')
    # textgen.generate(interactive=True, top_n=5)
    # textgen.generate(3, temperature=1.0)

    from textgenrnn import textgenrnn
    textgen = textgenrnn(weights_path='data/colaboratory_weights.hdf5',
                     vocab_path='data/colaboratory_vocab.json',
                     config_path='data/colaboratory_config.json')

    textgen.generate_samples(max_gen_length=1000)
    textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

if __name__ == '__main__':
    main()
