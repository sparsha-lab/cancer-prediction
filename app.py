from flask import Flask, render_template,request
import pickle
app = Flask(__name__)
with open("lr_cancer_model.pkl","rb")as file:
    lr_model=pickle.load(file)
def cancerPrediction(radius_mean=0.2, texture_mean=0.4, perimeter_mean=0.2,area_mean=0.4, smoothness_mean=0.5, compactness_mean=0.3, concavity_mean=0.72,concave_points_mean=0.11, symmetry_mean=0.43, fractal_dimension_mean=0.23,radius_se=0.123, texture_se=0.32, perimeter_se=0.98, area_se=0.99, smoothness_se=0.43,compactness_se=0.34, concavity_se=0.12, concave_points_se=0.78, symmetry_se=0.345,fractal_dimension_se=0.345, radius_worst=0.234, texture_worst=0.67,perimeter_worst=0.45, area_worst=0.23, smoothness_worst=0.34, compactness_worst=0.54, concavity_worst=0.23, concave_points_worst=0.1,symmetry_worst=0.25, fractal_dimension_worst=0.1):
    lst=[]
    lst=lst+[radius_mean]
    lst=lst+[texture_mean]
    lst=lst+[perimeter_mean]
    lst=lst+[area_mean]
    lst=lst+[smoothness_mean]
    lst=lst+[compactness_mean]
    lst=lst+[concavity_mean]
    lst=lst+[concave_points_mean]
    lst=lst+[symmetry_mean]
    lst=lst+[fractal_dimension_mean]
    lst=lst+[radius_se]
    lst=lst+[texture_se]
    lst=lst+[perimeter_se]
    lst=lst+[area_se]
    lst=lst+[smoothness_se]
    lst=lst+[compactness_se]
    lst=lst+[concavity_se]
    lst=lst+[concave_points_se]
    lst=lst+[symmetry_se]
    lst=lst+[fractal_dimension_se]
    lst=lst+[radius_worst]
    lst=lst+[texture_worst]
    lst=lst+[perimeter_worst]
    lst=lst+[area_worst]
    lst=lst+[smoothness_worst]
    lst=lst+[compactness_worst]
    lst=lst+[concavity_worst]
    lst=lst+[concave_points_worst]
    lst=lst+[symmetry_worst]
    lst=lst+[fractal_dimension_worst]
    # lst=lst+[]
    #lst=sc.transfrom([[lst]])
    
    result=lr_model.predict([lst])
    
    
    if result==0:
        return "B"
    elif result==1:
        return "M"
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict")
def predict():
    if request.method == "POST":
        # Collect form inputs
        radius_mean = float(request.form.get("radius_mean"))
        texture_mean = float(request.form.get("texture_mean"))
        perimeter_mean = float(request.form.get("perimeter_mean"))
        area_mean = float(request.form.get("area_mean"))
        smoothness_mean = float(request.form.get("smoothness_mean"))
        compactness_mean = float(request.form.get("compactness_mean"))
        concavity_mean = float(request.form.get("concavity_mean"))
        concave_points_mean = float(request.form.get("concave_points_mean"))
        symmetry_mean = float(request.form.get("symmetry_mean"))
        fractal_dimension_mean = float(request.form.get("fractal_dimension_mean"))

        radius_se = float(request.form.get("radius_se"))
        texture_se = float(request.form.get("texture_se"))
        perimeter_se = float(request.form.get("perimeter_se"))
        area_se = float(request.form.get("area_se"))
        smoothness_se = float(request.form.get("smoothness_se"))
        compactness_se = float(request.form.get("compactness_se"))
        concavity_se = float(request.form.get("concavity_se"))
        concave_points_se = float(request.form.get("concave_points_se"))
        symmetry_se = float(request.form.get("symmetry_se"))
        fractal_dimension_se = float(request.form.get("fractal_dimension_se"))

        radius_worst = float(request.form.get("radius_worst"))
        texture_worst = float(request.form.get("texture_worst"))
        perimeter_worst = float(request.form.get("perimeter_worst"))
        area_worst = float(request.form.get("area_worst"))
        smoothness_worst = float(request.form.get("smoothness_worst"))
        compactness_worst = float(request.form.get("compactness_worst"))
        concavity_worst = float(request.form.get("concavity_worst"))
        concave_points_worst = float(request.form.get("concave_points_worst"))
        symmetry_worst = float(request.form.get("symmetry_worst"))
        fractal_dimension_worst = float(request.form.get("fractal_dimension_worst"))

        # Call your ML prediction function
        result = cancerPrediction(
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
            radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
            compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
        )

        return render_template("predict.html", prediction=result)

    return render_template("predict.html")

   

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


