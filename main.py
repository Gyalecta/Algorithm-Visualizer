import random
import time
import threading
import tkinter as tk

class SortingVisualizer:
    def __init__(self, window, width=1920, height=1080):
        self.window = window
        self.window.title("Sorting Visualizer")
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)
        self.window.config(bg="white")


        self.canvas = tk.Canvas(self.window, width=width, height=height-100, bg="#f5f5f5")
        self.canvas.pack()

        self.sorting_algorithm = tk.StringVar()
        self.sorting_algorithm.set("Bubble Sort")

        self.frame_buttons = tk.Frame(self.window, width=width, height=100, bg="white")
        self.frame_buttons.pack()

        self.button_bubble_sort = tk.Radiobutton(self.frame_buttons, text="Bubble Sort", variable=self.sorting_algorithm, value="Bubble Sort", bg="white", font=("Arial", 12))
        self.button_selection_sort = tk.Radiobutton(self.frame_buttons, text="Selection Sort", variable=self.sorting_algorithm, value="Selection Sort", bg="white", font=("Arial", 12))
        self.button_insertion_sort = tk.Radiobutton(self.frame_buttons, text="Insertion Sort", variable=self.sorting_algorithm, value="Insertion Sort", bg="white", font=("Arial", 12))
        self.button_quick_sort = tk.Radiobutton(self.frame_buttons, text="Quick Sort", variable=self.sorting_algorithm, value="Quick Sort", bg="white", font=("Arial", 12))
        self.button_merge_sort = tk.Radiobutton(self.frame_buttons, text="Merge Sort", variable=self.sorting_algorithm, value="Merge Sort", bg="white", font=("Arial", 12))
        self.button_start = tk.Button(self.frame_buttons, text="Start", command=self.start_sorting, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.button_stop = tk.Button(self.frame_buttons, text="Stop", command=self.stop_sorting, bg="#f44336", fg="white", font=("Arial", 12))
        self.button_quit = tk.Button(self.frame_buttons, text="Quit", command=self.window.quit, bg="#607d8b", fg="white", font=("Arial", 12))

        self.button_bubble_sort.pack(side=tk.LEFT, padx=10)
        self.button_selection_sort.pack(side=tk.LEFT, padx=10)
        self.button_insertion_sort.pack(side=tk.LEFT, padx=10)
        self.button_quick_sort.pack(side=tk.LEFT, padx=10)
        self.button_merge_sort.pack(side=tk.LEFT, padx=10)
        self.button_start.pack(side=tk.LEFT, padx=10)
        self.button_stop.pack(side=tk.LEFT, padx=10)
        self.button_quit.pack(side=tk.LEFT, padx=10)

        self.array = []

    def generate_array(self):
        self.array = []
        for _ in range(100):
            self.array.append(random.randint(1, 100))
        self.draw_array(self.array)

    def draw_array(self, array):
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(array)
        offset = 5
        for i in range(len(array)):
            x0 = i * bar_width + offset
            y0 = canvas_height - (array[i] / 100) * (canvas_height - offset)
            x1 = (i + 1) * bar_width - offset
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#4CAF50")
            self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(array[i]), font=("Arial", 10))

    def start_sorting(self):
        self.generate_array()
        if self.sorting_algorithm.get() == "Bubble Sort":
            self.bubble_sort()
        elif self.sorting_algorithm.get() == "Selection Sort":
            self.selection_sort()
        elif self.sorting_algorithm.get() == "Insertion Sort":
            self.insertion_sort()
        elif self.sorting_algorithm.get() == "Quick Sort":
            self.quick_sort()
        elif self.sorting_algorithm.get() == "Merge Sort":
            self.merge_sort()

    def stop_sorting(self):
        self.window.destroy()

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array(self.array)
                    time.sleep(0.01)
        self.draw_array(self.array)

    def selection_sort(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.draw_array(self.array)
            time.sleep(0.01)
        self.draw_array(self.array)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array(self.array)
            time.sleep(0.01)
        self.draw_array(self.array)

    def quick_sort(self):
        self.quick_sort_helper(0, len(self.array) - 1)
        self.draw_array(self.array)

    def quick_sort_helper(self, start, end):
        if start >= end:
            return
        pivot = self.partition(start, end)
        self.quick_sort_helper(start, pivot - 1)
        self.quick_sort_helper(pivot + 1, end)

    def partition(self, start, end):
        pivot = self.array[end]
        pivot_index = start
        for i in range(start, end):
            if self.array[i] < pivot:
                self.array[i], self.array[pivot_index] = self.array[pivot_index], self.array[i]
                pivot_index += 1
        self.array[pivot_index], self.array[end] = self.array[end], self.array[pivot_index]
        self.draw_array(self.array)
        time.sleep(0.01)
        return pivot_index
    
    def merge_sort(self):
        self.merge_sort_helper(0, len(self.array) - 1)
        self.draw_array(self.array)

    def merge_sort_helper(self, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort_helper(start, mid)
        self.merge_sort_helper(mid + 1, end)
        self.merge(start, mid, end)

    def merge(self, start, mid, end):
        left = self.array[start:mid + 1]
        right = self.array[mid + 1:end + 1]
        left_index = right_index = 0
        for i in range(start, end + 1):
            if left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    self.array[i] = left[left_index]
                    left_index += 1
                else:
                    self.array[i] = right[right_index]
                    right_index += 1
            elif left_index < len(left):
                self.array[i] = left[left_index]
                left_index += 1
            elif right_index < len(right):
                self.array[i] = right[right_index]
                right_index += 1
        self.draw_array(self.array)
        time.sleep(0.01)

    def quit(self):
        self.window.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sorting Algorithms Visualizer")
    root.geometry("900x600")
    app = SortingVisualizer(root)
    root.mainloop()