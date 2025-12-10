import datetime

def calculate_compound_interest(P, r, t, n=12):
    """Расчёт итоговой суммы по формуле сложных процентов"""
    try:
        if P <= 0 or r <= 0 or t <= 0:
            raise ValueError("Все значения должны быть положительными")

        r = r / 100  # Преобразуем ставку в доли
        S = P * (1 + r / n) ** (n * t)
        return S

    except Exception as e:
        log_error(f"Ошибка при расчете: {e}")
        return None


def log_error(message):
    """Запись ошибок в файл errors.log"""
    with open("errors.log", "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        f.write(f"{timestamp} - ERROR - {message}\n")


def main():
    try:
        # Ввод данных пользователем
        P = float(input("Введите сумму вклада: "))
        r = float(input("Введите годовую ставку (%): "))
        t = float(input("Введите срок вклада (в годах): "))

        # Расчёт
        S = calculate_compound_interest(P, r, t)

        if S is not None:
            print(f"\nИтоговая сумма через {int(t)} лет: {S:.2f} тенге")
            print("Работа программы завершена.\n")

            # Запись результата в result.txt
            with open("result.txt", "a", encoding="utf-8") as file:
                file.write(
                    f"\nВклад: {P} тг\n"
                    f"Ставка: {r}%\n"
                    f"Срок: {int(t)} лет\n"
                    f"Итоговая сумма: {S:.2f} тг\n"
                )

    except ValueError:
        log_error("Ошибка при вводе: необходимо ввести числовые значения")
        print("Ошибка: введите числовые значения.")
    except ZeroDivisionError:
        log_error("Ошибка при расчете: деление на ноль")
        print("Ошибка: деление на ноль.")
    except Exception as e:
        log_error(f"Неизвестная ошибка: {e}")
        print("Произошла ошибка. Проверьте данные и попробуйте снова.")


if __name__ == "__main__":
    main()
