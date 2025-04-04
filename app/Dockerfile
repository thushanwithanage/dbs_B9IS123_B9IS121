# Use a Node.js base image
FROM node:14-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json from the current folder (app-directory)
COPY package*.json ./

# Install the dependencies inside the container
RUN npm install

# Copy all other application code into the container
COPY . .

# Expose the port your app will run on (3000 in this case)
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]