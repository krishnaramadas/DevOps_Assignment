# Create the base image
FROM python:3.8

# Change the working directory
WORKDIR /simple_calculator

# Install Dependency
COPY .  /simple_calculator
RUN pip install -r ./requirements.txt


# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["calculator_app.py"]

#Expose the post 5000.
EXPOSE 8000
