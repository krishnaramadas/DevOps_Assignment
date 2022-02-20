# Create the base image
FROM python:3.8

# Change the working directory
WORKDIR /simple_calculator

# Install Dependency
COPY requirements.txt /simple_calculator/
RUN pip install -r ./requirements.txt

# Copy local folder into the container
COPY calculator_app.py /simple_calculator/
COPY calculator.py /simple_calculator/
COPY test_calculator.py /simple_calculator/
COPY templates/index.html /app/templates/index.html

# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["calculator_app.py"]

#Expose the post 5000.
EXPOSE 8000
