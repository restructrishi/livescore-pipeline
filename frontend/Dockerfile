# Use an official Nginx image
FROM nginx:1.21-alpine

# Copy our static website files
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Remove the default Nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy our custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/