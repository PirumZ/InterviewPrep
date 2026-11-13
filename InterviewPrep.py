# # # # def average(numbers):
# # # #     total = 0
# # # #
# # # #     if not numbers:
# # # #         raise ValueError("Numbers does not have any members.")
# # # #
# # # #     for number in numbers:
# # # #         total = number
# # # #
# # # #     return total / len(numbers)
# # # #
# # # #
# # # # items = ["A", "B", "A", "C", "B", "D"]
# # # # found_items = []
# # # #
# # # # for item in items:
# # # #     if item not in found_items:
# # # #         found_items.append(item)
# # # #
# # # # #print(found_items)
# # # #
# # # #
# # # # nums = [10,20,30]
# # # #
# # # #
# # # # transactions = [
# # # #     {"customer_id": 10, "amount": 120},
# # # #     {"customer_id": 20, "amount": 80},
# # # #     {"customer_id": 10, "amount": 200},
# # # #     {"customer_id": 30, "amount": 150},
# # # #     {"customer_id": 20, "amount": 100}
# # # # ]
# # # #
# # # # customer_amounts = {}
# # # #
# # # # for transaction in transactions:
# # # #     customer_id = transaction["customer_id"]
# # # #     amount = transaction["amount"]
# # # #
# # # #     if customer_id not in customer_amounts:
# # # #         customer_amounts[customer_id] = amount
# # # #     elif customer_id in customer_amounts:
# # # #         # aware the elif isn't explicitly necessary, just for personal benefit
# # # #         customer_amounts[customer_id] += amount
# # # #
# # # # #print(customer_amounts)
# # # #
# # # # highest_customer = None
# # # # highest_amount = 0
# # # #
# # # # for key, value in customer_amounts.items():
# # # #     if value > highest_amount:
# # # #         highest_amount = value
# # # #         highest_customer = key
# # # #
# # # # #print(f"The most abused customer is Customer ID: {highest_customer}, Sum: {highest_amount}")
# # # #
# # # #
# # # # sales = [
# # # #     {"department": "IT", "amount": 120},
# # # #     {"department": "Sales", "amount": 80},
# # # #     {"department": "IT", "amount": 200},
# # # #     {"department": "HR", "amount": 150},
# # # #     {"department": "Sales", "amount": 100},
# # # #     {"department": "IT", "amount": 50}
# # # # ]
# # # # department_totals = {}
# # # #
# # # #
# # # # for sale in sales:
# # # #     department_id = sale["department"]
# # # #     amount = sale["amount"]
# # # #
# # # #     #if department_id not in department_totals:
# # # #     #    department_totals[department_id] = amount
# # # #     #else:
# # # #     #    department_totals[department_id] += amount
# # # #
# # # #     department_totals[department_id] = department_totals.get(department_id, 0) + amount
# # # #
# # # # #for dept, total in department_totals.items():
# # # # #    print(f"{dept}: {total}")
# # # #
# # # #
# # # # employees = [
# # # #     {"name": "Alice", "department": "IT", "salary": 70000},
# # # #     {"name": "Bob", "department": "Sales", "salary": 55000},
# # # #     {"name": "Carol", "department": "IT", "salary": 85000},
# # # #     {"name": "Dave", "department": "IT", "salary": None},
# # # #     {"name": "Eve", "department": "Sales", "salary": 65000},
# # # #     {"name": "Frank", "department": "HR", "salary": 60000}
# # # # ]
# # # #
# # # # threshold = 65000
# # # #
# # # # def get_employees_over_threshold(cc_employees, threshold):
# # # #     employees_over_threshold = []
# # # #     for employee in cc_employees:
# # # #         name = employee["name"]
# # # #         salary = employee["salary"]
# # # #
# # # #         if salary is None:
# # # #             continue
# # # #         if salary >= threshold:
# # # #             employees_over_threshold.append(name)
# # # #
# # # #     return employees_over_threshold
# # # #
# # # # print(get_employees_over_threshold(employees, threshold))
# # # from shlex import split
# # #
# # # sales = [
# # #      {"department": "IT", "amount": 120},
# # #      {"department": "Sales", "amount": 80},
# # #      {"department": "IT", "amount": 200},
# # #      {"department": "HR", "amount": None},
# # #      {"department": "Sales", "amount": 100},
# # #      {"department": None, "amount": 50},
# # #      {"department": "IT", "amount": 50}
# # # ]
# # # #
# # # # def get_department_totals(sales_list):
# # # #     department_total_sales = {}
# # # #
# # # #
# # # #     for sale in sales_list:
# # # #
# # # #         department = sale["department"]
# # # #         amount = sale["amount"]
# # # #
# # # #         if department is None or amount is None:
# # # #             continue
# # # #
# # # #         if department not in department_total_sales:
# # # #             department_total_sales[department] = amount
# # # #         else:
# # # #             department_total_sales[department] += amount
# # # #
# # # #
# # # #     return department_total_sales
# # # #
# # # # print(get_department_totals(sales))
# # #
# # # # def get_departments_above_threshold(sales_list, threshold):
# # # #     department_totals = {}
# # # #     departments_above_threshold = []
# # # #
# # # #     for sale in sales_list:
# # # #         department = sale["department"]
# # # #         amount = sale["amount"]
# # # #
# # # #         if department is None or amount is None:
# # # #             continue
# # # #
# # # #         if department not in department_totals:
# # # #             department_totals[department] = amount
# # # #         else:
# # # #             department_totals[department] += amount
# # # #
# # # #     for department, total in department_totals.items():
# # # #         if total > threshold:
# # # #             departments_above_threshold.append(department)
# # # #
# # # #     return departments_above_threshold
# # # #
# # # #
# # # # print(get_departments_above_threshold(sales, 200))
# # #
# # #
# # # # transactions = [
# # # #     {"id": 101, "status": "complete"},
# # # #     {"id": 102, "status": "failed"},
# # # #     {"id": 103, "status": "complete"},
# # # #     {"id": 104, "status": None},
# # # #     {"id": 105, "status": "pending"},
# # # #     {"id": 106, "status": "failed"},
# # # #     {"id": 107, "status": "complete"},
# # # #     {"id": 108}
# # # # ]
# # # #
# # # # def count_transaction_statuses(transactions):
# # # #     status_records = {}
# # # #     for transaction in transactions:
# # # #
# # # #         status = transaction.get("status")
# # # #
# # # #         if status is None:
# # # #             continue
# # # #
# # # #         status_records[status] = status_records.get(status, 0) + 1
# # # #
# # # #     return status_records
# # # #
# # # # print(count_transaction_statuses(transactions))
# # #
# # #
# # # # logs = [
# # # #     "2026-10-20 INFO Server started",
# # # #     "2026-10-20 ERROR Database connection failed",
# # # #     "2026-10-20 INFO Request received",
# # # #     "2026-10-20 ERROR Timeout occurred",
# # # #     "2026-10-20 WARNING High memory usage",
# # # #     "2026-10-20 INFO Request completed"
# # # # ]
# # # #
# # # # def count_log_levels(logs):
# # # #     log_records = {}
# # # #     for log in logs:
# # # #
# # # #         log_level = log.split()[1]
# # # #         log_records[log_level] = log_records.get(log_level, 0) + 1
# # # #
# # # #     return log_records
# # # #
# # # #
# # # #
# # # # print(count_log_levels(logs))
# # #
# # # records = [
# # #      {"id": 101, "name": "Alice"},
# # #      {"id": 102, "name": "Bob"},
# # #      {"id": 103, "name": "Carol"},
# # #      {"id": 101, "name": "Alice"},
# # #      {"id": 104, "name": "Dave"},
# # #      {"id": 102, "name": "Bob"},
# # #      {"id": 105, "name": "Eve"}
# # # ]
# # #
# # # def find_duplicate_ids(records):
# # #      seen_ids = {}
# # #      for record in records:
# # #           record_id = record.get("id")
# # #
# # #           seen_ids[record_id] = seen_ids.get(record_id, 0) + 1
# # #
# # #      duplicate_keys = []
# # #      for key, value in seen_ids.items():
# # #           if value > 1:
# # #                duplicate_keys.append(key)
# # #
# # #      return duplicate_keys
# # #
# # # print(find_duplicate_ids(records))
# #
# # logs = [
# #     "2026-10-21 INFO Application started",
# #     "2026-10-21 ERROR Database connection failed",
# #     "2026-10-21 WARNING High memory usage",
# #     "2026-10-21 ERROR Request timed out",
# #     "2026-10-21 INFO Request completed"
# # ]
# #
# # def get_error_messages(logs):
# #      error_logs = []
# #      for log in logs:
# #          log_parts = log.split()
# #          if log_parts[1] == "ERROR":
# #               msg = " ".join(log_parts[2:])
# #               error_logs.append(msg)
# #
# #      return error_logs
# #
# # print(get_error_messages(logs))
# #
#
# activity = [3, 5, 2, 0, 4, 6, 7, 0, 1, 2, 3, 4]
#
# def longest_run(activity):
#     streak = 0
#     longest_streak = 0
#     for num in activity:
#         if num == 0:
#             streak = 0
#         else:
#             streak += 1
#
#         if streak > longest_streak:
#             longest_streak = streak
#
#     return longest_streak
#
# print(longest_run(activity))

transactions = [
    {"customer_id": 101, "date": "2026-10-18", "amount": 50},
    {"customer_id": 102, "date": "2026-10-19", "amount": 80},
    {"customer_id": 101, "date": "2026-10-20", "amount": 120},
    {"customer_id": 102, "date": "2026-10-17", "amount": 40},
    {"customer_id": 103, "date": "2026-10-21", "amount": 65},
    {"customer_id": 101, "date": "2026-10-19", "amount": 90}
]

def most_recent_transaction(transactions):
    most_recent_intermediary = {}
    for transaction in transactions:
        customer_id = transaction.get("customer_id")
        date = transaction.get("date")
        amount = transaction.get("amount")
        if customer_id not in most_recent_intermediary:
            most_recent_intermediary[customer_id] = {"date": date, "amount": amount}
        else:
            if most_recent_intermediary[customer_id].get("date") < date:
                most_recent_intermediary[customer_id] = {"date": date, "amount": amount}

    most_recent = {}
    for customer_id in most_recent_intermediary:
        most_recent[customer_id] = most_recent_intermediary[customer_id].get("amount")

    return most_recent

print(most_recent_transaction(transactions))