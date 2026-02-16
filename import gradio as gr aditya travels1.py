import gradio as gr
class CarAgency:
    def __init__(self, name, available_car):
        self.name=name
        self.available_car=available_car

def create_car_agency(name, available_car):
    car_agency1=CarAgency(name, available_car)
    return f"Car Agency Name: {car_agency1.name}\nAvailable Car: {car_agency1.available_car}"

app=gr.Interface(
    fn=create_car_agency,
    inputs=[
        gr.Textbox(label="Enter Car Agency Name"),
        gr.Textbox(label="Enter Available Car")
    ],
    outputs=gr.Textbox(label="Car Agency Details"),
    title="ADITYA TRAVELS",
    description="Enter car agency name and available car to see details using class & object"
)   

app.launch()