import mysql.connector  # type:ignore


def connect_db():
    connection = mysql.connector.connect(host="localhost", user="root", password="Sunaymd@12", database="todo_app")
    return connection


def add_task(title, description):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "insert into tasks (title, description) values (%s, %s)"
    cursor.execute(sql, (title, description))
    conn.commit()
    print("Task added successfully!")
    cursor.close()
    conn.close()


def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"{task[0]}. {task[1]} - {task[2]} ({task[3]})")
    cursor.close()
    conn.close()


def update_task(task_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "UPDATE tasks SET status = %s WHERE id = %s"
    cursor.execute(sql, (status, task_id))
    conn.commit()
    print("Task updated successfully!")
    cursor.close()
    conn.close()


def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(sql, (task_id,))
    conn.commit()
    print("Task deleted successfully!")
    cursor.close()
    conn.close()


def menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            status = input("Enter new status (Pending/Completed): ")
            update_task(task_id, status)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
