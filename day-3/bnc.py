import random


def generate_unique_number():
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:4])


def calculate_bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows


def bulls_and_cows_game():
    secret_number = generate_unique_number()
    print('Загадано 4-х значное число, без повторяющихся цифр.')
    print('Попробуйте угадать число за 10 попыток.')

    log = []
    attempts = 0
    previous_guesses = set()

    while attempts < 10:
        user_guess = input("Введите ваше предположение: ")
        if user_guess == 's':
            print(f'Загаданное число: {secret_number}')
            break

        if user_guess == 'log':
            print(*log, sep='\n')
            continue

        if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:
            print('Число должно состоять из 4 уникальных цифр!!!')
            continue

        if user_guess in previous_guesses:
            print('Такое число уже было!!!')
            continue

        previous_guesses.add(user_guess)
        attempts += 1

        if user_guess == secret_number:
            print(f'Вы угадали число за {attempts} попыток!')
            break

        bulls, cows = calculate_bulls_and_cows(secret_number, user_guess)
        print(f'b{bulls} c{cows}')
        log.append(f'b{bulls}c{cows} {user_guess}')

    if attempts == 10 and user_guess != secret_number:
        print(f'Вы исчерпали все попытки! Загаданное число было: {secret_number}')


if __name__ == "__main__":
    bulls_and_cows_game()