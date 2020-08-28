mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = process.env.PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
