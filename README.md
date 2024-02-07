# ai_csv_parsing

currently at proof of concept stage  

run the app:  
run docker compose and go to localhost:5000  
first request very slow (pulling model)  
other requests not too fast either (running on mistral 7b for hardware reasons)  

TODOS:  
    -leverage batch edits provided by pandas  
    -implement ModelFile for better results for the specified purpose  
    -change api entry to be json rather than formdata (currently formdata to focus on learning ollama)  
    -create config file (change model, dev stage, port, etc..)  
    -add test features (return outputs for a few random lines => Adapt promp accordingly)  

