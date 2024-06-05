import argparse
import subprocess
import threading
import os

# Hàm để phân tích cú pháp các đối số dòng lệnh
def parse_args():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-username",
                        dest="username",
                        help="List username.",
                        
                        required=True,
                        action='store')
    
    args = parser.parse_args()
    return args

# Hàm để chạy lệnh bên ngoài
def run_command(username, output):
    command = f"python3 main.py -user {username} -mode automatic -output {output} -ffmpeg"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr}")

# Danh sách các username
usernames1 = ["park.77m1","bonbarber2210","minhly06_01", "hunggymcalis", "quocvu93","nienty28", "buiquoc_sw","truongminhdung1904","anhhhh_tu","hongduong.1199"]
usernames2 = ["honguynvn04","365.ngy.nh.em","herst277","trinhatquankhu1","thang_masic","gymerteamhonda"]
usernames3 = ["duongkimochii","duongtapxo","congmanhfitness","_nmd04","hieuluoitap","fu_nguyen68"]
usernames4 = ["hmatuan9","huutinh103","anhbodoi6mui","ikram_rmdn","kieubanana","cokhiminhtrung"]
usernames5 = ["hpp358965","rforrachman","ntf_205","rhenz_win","ashuracalisthenicsteam","nihao22012003"]
usernames6 = ["tvc.gym","ngthanhlong021006","kenvo12022001","minhnam2004","minh.ha0102","tienfit"]
usernames7 = ["hy.calis","bimostreetworkout.id","kenvo12022001","vanbinh0906","duc_trong9x"]
usernames8 = ["hoanganh1112022","tuntl675", "yeuem2003n","thanabodxx","minh.ha0102","quang_fitness"]
usernames9 = ["chulongcuaemm","141201nth", "voquyhuyyy24102001","manhhiucute","hieuvilai2007","trun_trun.32"]
usernames10 = ["anhhhh_tu","tuanhamez","sinhan68","jdnummer1"]
# Mapping choices to actual lists
username_lists = {
    'usernames1': usernames1,
    'usernames2': usernames2,
    'usernames3': usernames3,
    'usernames4': usernames4,
    'usernames5': usernames5,
    'usernames6': usernames6,
    'usernames7': usernames7,
    'usernames8': usernames8,
    'usernames9': usernames9,
    'usernames10': usernames10
}

def main():
    args = parse_args()
    output = args.username
    # Lấy danh sách các username từ đối số dòng lệnh
    usernames = username_lists[args.username]


    # Tạo luồng cho mỗi username trong danh sách
    threads = []
    for username in usernames:
        thread = threading.Thread(target=run_command, args=(username, output))
        threads.append(thread)

    # Bắt đầu chạy các luồng
    for thread in threads:
        thread.start()

    # Đợi tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    print("Tất cả luồng đã hoàn thành.")

if __name__ == "__main__":
    main()