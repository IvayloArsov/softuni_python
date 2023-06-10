jury = int(input())
avg_score = 0
num_scores = 0
counter = 0
presentations = {}
while True:
    presentation = input()

    if presentation == 'Finish':
        break
    presentations[presentation] = 0

    for judge in range(1, jury+1):
        score = float(input())
        presentations[presentation] += score
        counter += 1
        avg_score += score
        num_scores += 1
    presentations[presentation] /= counter
    counter = 0
avg_score /= num_scores
for key, value in presentations.items():
    print(f'{key} - {value:.2f}.')
print(f"Student's final assessment is {avg_score:.2f}.")
