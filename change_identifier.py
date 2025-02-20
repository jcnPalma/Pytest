import tkinter as tk
from tkinter import ttk, filedialog
import csv
import os

class CSVProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Processor")
        self.root.state("zoomed")  # Maximize the window

		# Sample comment

        self.button_for = ["Live", "Test", "Process"]

        # Create three datasets with two columns each
        self.live_items = []
        self.test_items = []
        self.changed_items = []
        self.module_name = "untitled"

        # Configure grid to expand
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        btn = tk.Button(self.root, text="Export to PDF", command=self.export_to_csv, bg="green", fg="white")
        btn.grid(row=0, column=2, columnspan=3, padx=10, pady=5, sticky="nsew")

        self.create_table(self.test_items, "First Table", 1, 0)
        self.create_table(self.test_items, "Second Table", 1, 1)
        self.create_table(self.changed_items, "Third Table", 1, 2)

    def process_csv(self):
        if not self.test_items or not self.test_items:
            print("No data to process")
            return
        
        print("Processing Data")
        line_items_prod = [item[0] for item in self.live_items]
        line_items_test = [item[0] for item in self.test_items]

        not_in_prod = [item for item in line_items_test if item not in line_items_prod]
        in_both = [item for item in line_items_test if item in line_items_prod]

        format_changes = [item for item in in_both if self.test_items[line_items_test.index(item)][1] != self.live_items[line_items_prod.index(item)][1]]
        formula_changes = [item for item in in_both if self.test_items[line_items_test.index(item)][2] != self.live_items[line_items_prod.index(item)][2]]
        summary_changes = [item for item in in_both if self.test_items[line_items_test.index(item)][3] != self.live_items[line_items_prod.index(item)][3]]

        merged_list = not_in_prod + format_changes + formula_changes + summary_changes
        unique_merged_list = list(set(merged_list))

        new_data3 = [row for row in self.test_items if row[0] in unique_merged_list]
        self.update_table(self.changed_items, new_data3, 2)
        self.changed_items = new_data3

        print(self.module_name)

    def export_to_csv(self):
        print("Exporting to CSV")

        if not self.changed_items:
            print("No data to export")
            return
        
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        save_path = filedialog.askdirectory(initialdir=desktop_path)

        if not save_path:
            print("Save operation cancelled")
        else:
            file_path = os.path.join(save_path, f"{self.module_name}_changes.csv")
            file_path = os.path.normpath(file_path)  # Normalize path
            
            # Create and write an empty file (or overwrite if exists)
            with open(file_path, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(self.changed_items)
            
            print(f"File created: {file_path}")

    def open_file(self, from_where):
        if from_where == "Process":
            self.process_csv()
        else:
            file_path = filedialog.askopenfilename()

            csv_data = []

            with open(file_path, newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                row_no = 1
                for row in csvreader:
                    if row_no == 2:
                        self.module_name = row[0].replace(":", "_")
                        print(self.module_name)
                    elif row_no > 2:
                        row_to_append = (row[0], row[1], row[2], row[3], row[4])
                        csv_data.append(row_to_append)

                    row_no += 1

            # Update the specific table with new data
            if from_where == "Live":
                self.update_table(self.live_items, csv_data, 0)
                if self.test_items:
                    self.process_csv()
            elif from_where == "Test":
                self.update_table(self.test_items, csv_data, 1)
                if self.live_items:
                    self.process_csv()

    def update_table(self, table_data, new_data, column):
        table_data.clear()
        table_data.extend(new_data)

        # Find the corresponding treeview and update it
        for child in self.root.winfo_children():
            if isinstance(child, ttk.LabelFrame) and child.grid_info()["column"] == column:
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Treeview):
                        grandchild.delete(*grandchild.get_children())
                        for item in new_data:
                            grandchild.insert("", "end", values=(item[0], item[2]))

        return self

    def create_table(self, data, title, row, column):
        frame = ttk.LabelFrame(self.root, text=title)
        frame.grid(row=row, column=column, padx=10, pady=5, sticky="nsew")

        tree = ttk.Treeview(frame, columns=("Column1", "Column2"), show="headings")
        tree.heading("Column1", text="Column1")
        tree.heading("Column2", text="Column2")
        tree.column("Column1", width=100)
        tree.column("Column2", width=100)

        for item in data:
            tree.insert("", "end", values=item)

        tree.pack(expand=True, fill='both')

        # Add button below each table
        btn = ttk.Button(frame, text=f"Open {title}", command=lambda: self.open_file(self.button_for[column]))
        btn.pack(pady=5)

        return self

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVProcessorApp(root)
    root.mainloop()