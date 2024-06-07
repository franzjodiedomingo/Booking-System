import tkinter as tk
from tkinter import PhotoImage, LEFT
import customtkinter as Ctk
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkFont, CTkEntry
from datetime import datetime

class BookingWindow(tk.Toplevel):
    def __init__(self, master=None, vehicle_type=""):
        super().__init__(master)
        self.title(f"{vehicle_type} Booking Window")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(background="#C8E7F5")

        font2 = CTkFont(family="Inter", size=20)

        self.booking_window_frame = CTkFrame(self, width=449, height=434, border_width=2, fg_color="#F6D2E0")
        self.booking_window_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Pick-up Address
        self.pickup_label = CTkLabel(self.booking_window_frame, text="Pick-up Address:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.1, anchor="w")

        self.pickup_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.1, anchor="w")

        # Drop-off Address
        self.dropoff_label = CTkLabel(self.booking_window_frame, text="Drop-off Address:", text_color="#000000", font=font2)
        self.dropoff_label.place(relx=0.1, rely=0.2, anchor="w")

        self.dropoff_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.dropoff_entry.place(relx=0.5, rely=0.2, anchor="w")

        # Pick-up Date
        self.pickup_date_label = CTkLabel(self.booking_window_frame, text="Pick-up Date:", text_color="#000000", font=font2)
        self.pickup_date_label.place(relx=0.1, rely=0.3, anchor="w")

        self.pickup_date_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_date_entry.place(relx=0.5, rely=0.3, anchor="w")

        # Pick-up Time
        self.pickup_time_label = CTkLabel(self.booking_window_frame, text="Pick-up Time:", text_color="#000000", font=font2)
        self.pickup_time_label.place(relx=0.1, rely=0.4, anchor="w")

        self.pickup_time_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_time_entry.place(relx=0.5, rely=0.4, anchor="w")

        # Submit button
        self.submit_button = CTkButton(self.booking_window_frame, text="Submit", fg_color="#000000", text_color="#C8E7F5")
        self.submit_button.place(relx=0.5, rely=0.9, anchor="center")

        # Center the booking window
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

class RideApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Zoomers")

        # Fonts
        font1 = CTkFont(family="Candara", size=70, weight="bold", slant="italic")

        # Make the window resizable
        self.master.geometry("1200x1024")  # Initial size
        self.master.resizable(True, True)
        self.master.configure(bg="#F6D2E0")

        # Header frame (Logo, Name of the App) using customtkinter for a modern look
        self.header_frame = CTkFrame(master, corner_radius=10, fg_color="#C8E7F5", height=90, border_color="#C8E7F5", border_width=5)
        self.header_frame.pack(fill=tk.X)

        self.header_label = CTkLabel(self.header_frame, text="ZOOMERS", font=font1, text_color="#FFFFFF")
        self.header_label.place(relx=0.43, rely=0.5, anchor="w")

        self.header_img = tk.PhotoImage(file='zoomers_logo.png')
        self.header_image_label = CTkLabel(self.header_frame, image=self.header_img, fg_color="#C8E7F5")
        self.header_image_label.place(relx=0.35, rely=0.5, anchor="w")

        # Motor frame
        self.motor_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.motor_frame.place(relx=0.50, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Motor icon
        self.motor_img = tk.PhotoImage(file='motor.png')
        self.motor_image_label = tk.Label(self.motor_frame, image=self.motor_img, bg="#C8E7F5")
        self.motor_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Motor button
        self.motor_button = tk.Button(master, text="Book Motor", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Motor"))
        self.motor_button.place(relx=0.50, rely=0.49, anchor="center")

        # Car frame
        self.car_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.car_frame.place(relx=0.83, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Car icon
        self.car_img = tk.PhotoImage(file='car.png')
        self.car_image_label = tk.Label(self.car_frame, image=self.car_img, bg="#C8E7F5")
        self.car_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Car button
        self.car_button = tk.Button(master, text="Book Car", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Car"))
        self.car_button.place(relx=0.83, rely=0.49, anchor="center")

        # Taxi cab frame
        self.taxi_cab_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.taxi_cab_frame.place(relx=0.50, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Taxi cab icon
        self.taxi_cab_img = tk.PhotoImage(file='taxicab.png')
        self.taxi_cab_image_label = tk.Label(self.taxi_cab_frame, image=self.taxi_cab_img, bg="#C8E7F5")
        self.taxi_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Taxi cab button
        self.taxi_cab_button = tk.Button(master, text="Book Taxi Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Taxi Cab"))
        self.taxi_cab_button.place(relx=0.50, rely=0.89, anchor="center")

        # Premium cab frame
        self.prem_cab_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.prem_cab_frame.place(relx=0.83, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Premium cab icon
        self.prem_cab_img = tk.PhotoImage(file='premcab.png')
        self.prem_cab_image_label = tk.Label(self.prem_cab_frame, image=self.prem_cab_img, bg="#C8E7F5")
        self.prem_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Premium cab button
        self.prem_cab_button = tk.Button(master, text="Book Premium Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Premium Cab"))
        self.prem_cab_button.place(relx=0.83, rely=0.89, anchor="center")

        # Profile button
        self.profile_button = tk.Button(master, text="PROFILE", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.profile_button.place(relx=0.30, rely=0.15, anchor="ne")

        # Bookings button
        self.bookings_button = tk.Button(master, text="BOOKINGS", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.bookings_button.place(relx=0.30, rely=0.30, anchor="ne")

        # History button
        self.history_button = tk.Button(master, text="HISTORY", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.history_button.place(relx=0.30, rely=0.45, anchor="ne")

        # Feedback button
        self.feedback_button = tk.Button(master, text="FEEDBACK", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.feedback_button.place(relx=0.30, rely=0.60, anchor="ne")

        # Log-out Button
        self.out_button = tk.Button(master, text="LOG OUT", font=("Candara", 20, "bold"), height=2, width=20, fg="#FFFFFF", bg="#000000")
        self.out_button.place(relx=0.30, rely=0.75, anchor="ne")

        # Bind the label and frame together
        self.prem_cab_frame.bind("<Configure>", self.on_frame_configure)
        self.prem_cab_image_label.bind("<Configure>", self.on_label_configure)

    def on_frame_configure(self, event):
        # Get the new size of the frame
        width = event.width
        height = event.height

        # Adjust the size of the label to match the frame
        self.prem_cab_image_label.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def on_label_configure(self, event):
        # Get the new size of the label
        width = event.width
        height = event.height

        # Adjust the size of the frame to match the label
        self.prem_cab_frame.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def show_vehicle_details(self, vehicle_type):
        details = {
            "Motor": ("Zoom-Wheel: Fast and Stress-Free!\n"
              "\n"
              "• Enjoy motorbike rides on-demand.\n"
              "\n"
              "• Arrive at your destination smoothly.\n"
              "\n"
              "• Experience the easy booking.",
              "MOTORPIC.png"),

            "Car": ("Zoom-Zone: Travel with a Zing!\n\n"
                    "\n"
                    "• Effortless journeys with our fleet.\n"
                    "\n"
                    "• Various vehicles for your comfort.\n"
                    "\n"
                    "• Flexible easy payment methods.",
                    "CARPIC.png"),

            "Taxi Cab": ("Zoom-Cab: Lightning-Fast Rides!\n\n"
                         "\n"
                         "• Effortless booking for rapid transit.\n"
                         "\n"
                         "• Choose from standard and premium rides.\n"
                         "\n"
                         "• Metered fare with a minimal booking fee.",
                         "TAXICABPIC.png"),

            "Premium Cab": ("Zoom-Wheel: Accelerating Your Commute!\n\n"
                            "• Swift transportation! (5 seater)\n"
                            "\n"
                            "• Onboard Wi-Fi for productive journeys.\n"
                            "\n"
                            "• Transparent pricing with no hidden fees.",
                            "PREMIUMCABPIC.png")
        }

        detail_text, image_file = details.get(vehicle_type, ("No details available", ""))

        popup = tk.Toplevel(self.master)
        popup.title(f"{vehicle_type} Details")
        popup.geometry("500x650")
        popup.configure(bg="#C8E7F5")

        header, details = detail_text.split('\n\n', 1)

        header_label = tk.Label(popup, text=header, font=("Candara", 16, "bold"), bg="#C8E7F5", justify="center")
        header_label.place(relx=0.5, rely=0.08, anchor="center", relwidth=0.9)

        detail_label = tk.Label(popup, text=details, font=("Lucida Console", 11), bg="#C8E7F5", justify=LEFT, wraplength=450, pady=5)
        detail_label.place(relx=0.5, rely=0.71, anchor="center", relwidth=0.9)

        if image_file:
            image = PhotoImage(file=image_file)
            image_label = tk.Label(popup, image=image, bg="#C8E7F5")
            image_label.image = image
            image_label.place(relx=0.5, rely=0.37, anchor="center")

        book_button = tk.Button(popup, text="BOOK NOW", font=("Helvetica", 13, "bold"), bg="#F6D2E0", command=lambda: self.open_booking_window(vehicle_type, popup))
        book_button.place(relx=0.5, rely=0.86, anchor="center", relwidth=0.6)

        close_button = tk.Button(popup, text="CANCEL", font=("Helvetica", 11), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.92, anchor="center", relwidth=0.6)

        self.center_popup(popup)

    def center_popup(self, popup):
        popup.update_idletasks()
        width = popup.winfo_width()
        height = popup.winfo_height()
        x = (popup.winfo_screenwidth() // 2) - (width // 2)
        y = (popup.winfo_screenheight() // 2) - (height // 2)
        popup.geometry(f"{width}x{height}+{x}+{y}")

    def open_booking_window(self, vehicle_type, popup):
        popup.destroy()  # Close the details popup
        booking_window = BookingWindow(self.master, vehicle_type)

root = tk.Tk()
app = RideApp(root)
root.mainloop()