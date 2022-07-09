class WordsPriorityCalculations:
    @staticmethod
    def get_words_classic(method_freq_dict, user_freq_dict, number_of_words, coef_cancel=1) -> list:
        result = []

        # sort dictinary by rating
        method_freq_dict = {k: v for k, v in sorted(method_freq_dict.items(), key=lambda item: item[1], reverse=True)}

        method_freq_dict = {k: method_freq_dict[k] for k in
                            list(method_freq_dict)[:len(user_freq_dict) + number_of_words]}

        for key, value in user_freq_dict.items():
            if value >= coef_cancel:
                if key in method_freq_dict:
                    del method_freq_dict[key]

        return list(method_freq_dict.keys())[:number_of_words]
