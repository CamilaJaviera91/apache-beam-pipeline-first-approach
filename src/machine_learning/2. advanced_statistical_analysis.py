import numpy as np
import pandas as pd
import scipy.stats as stats

# Load the dataset from the specified CSV file.
df = pd.read_csv('./src/download/chins_filtered_7.csv')

def hypothesis_testing(value_mean, name_mean):
    for i, mean in enumerate(value_mean):
        # Wrap around when accessing the next mean and its corresponding name
        next_i = (i + 1) % len(value_mean)
        next_mean = value_mean[next_i]
        next_name = name_mean[next_i]

        print(f"Mean {name_mean[i]}: {mean}")
        print(f"Mean {next_name}: {next_mean}")

        # Generate random data for group_a and group_b with the current and next mean
        group_a = np.random.normal(loc=mean, scale=10, size=30)
        group_b = np.random.normal(loc=next_mean, scale=10, size=30)

        # Perform t-test
        t_stat, p_value = stats.ttest_ind(group_a, group_b)
        
        print(f"T-statistic: {t_stat:.4f}")
        print(f"P-value: {p_value:.4f}")

        if p_value < 0.05:
            print("We reject the null hypothesis: the means are significantly different.")
        else:
            print("There is not enough evidence to reject the null hypothesis.")

        print('\n')

if __name__ == '__main__':
    # Calculate the means
    value_mean = [float(df['Situps'].mean()), float(df['Jumps'].mean()), float(df['Chins'].mean())]
    name_mean = ['Situps', 'Jumps', 'Chins']

    # Call hypothesis testing function
    hypothesis_testing(value_mean, name_mean)
