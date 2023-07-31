#! /bin/bash

print_test_cases() {
    echo "Usage: $0 [ { -t | --test } <test_case> ... ] [ { -d | --device_name } <device_name> ]"
    echo "Options:"
    echo "  -h, --help        Show help message"
    echo "  -t, --test_case   Add test case to be run"
    echo "  -d, --device_name Name of tested device"
    echo ""
    echo "Available Test Cases:"
    echo "1. test_four_add_eight"
    echo "2. test_nine_div_three"
    echo "3. test_zero_div"
    echo "4. test_root_from_negative"
}

run_test() {
    python test_calculator.py "$@"
}

TEST_CASE=""
DEVICE_NAME=""

# test_calculator.bash -t t1 t2 t3 -d dev
for var in "$@"
do
   case "$var" in
        -h|--help)
            print_test_cases
            exit 0
            ;;
        -t|--test)
            IS_TEST="1"
            IS_DEVICE="0"
            ;;
        -d|--device_name)
            IS_DEVICE="1"
            IS_TEST="0"
            ;;
        *)
            if [ "$IS_TEST" -eq "1" ]; then
                TEST_CASE="$TEST_CASE -t $var"
            fi
            if [ "$IS_DEVICE" -eq "1" ]; then
                DEVICE_NAME="-d $var"
            fi
            ;;
    esac
done


run_test $TEST_CASE $DEVICE_NAME
