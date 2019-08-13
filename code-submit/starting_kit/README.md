sudo docker run -v $(pwd):/app/kit -it chuanlinlan/lenet
cd app/kit/
python3 ingestion_program/ingestion.py
python3 scoring_program/score.py


