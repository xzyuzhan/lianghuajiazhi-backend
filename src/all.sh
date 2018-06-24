python a00_get_a_all_pb_to_csv_json.py

python a10_get_top100.py

python a20_get_history_pb.py

python a30_merge_result.py

python a90_show_risk_level.py

./high.sh
./middle.sh
./low.sh


./middle_3jlt.sh
./low_3jlt.sh

python csv2json.py top100.csv
python csv2json.py top100_high_all.csv
python csv2json.py top100_middle_all.csv
python csv2json.py top100_low_all.csv
python csv2json.py top100_middle_3jlt.csv
python csv2json.py top100_low_3jlt.csv

./copydata_to_website_gupiaoapp2.sh
