this_file=$(realpath $0)
dir_name=$(dirname $this_file)

source $dir_name/venv/bin/activate
$dir_name/pytelebot.py "$@"
