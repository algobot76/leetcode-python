class Solution:
    def reorderLogFiles(self, logs):
        if not logs:
            return []

        letter_logs = [log for log in logs if
                       log[log.index(' ') + 1].isalpha()]
        digit_logs = [log for log in logs if log[log.index(' ') + 1].isdigit()]
        letter_logs.sort(
            key=lambda log: (' '.join(log.split()[1:]), log.split()[0]))
        return letter_logs + digit_logs
