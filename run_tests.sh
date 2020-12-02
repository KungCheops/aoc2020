for day in $@
do
    cd "day${day}"
    test_result=$(python3 day${day}.py 1 test.txt)
    expected_result=$(cat test_result_1.txt)
    if [ $test_result != $expected_result ]
    then
        echo "============================================================"
        echo "Test failed"
        echo "Day $day part 1"
        echo "Expected $expected_result but got $test_result"
        echo "============================================================"
    fi
    test_result=$(python3 day${day}.py 2 test.txt)
    expected_result=$(cat test_result_2.txt)
    if [ $test_result != $expected_result ]
    then
        echo "============================================================"
        echo "Test failed"
        echo "Day $day part 2"
        echo "Expected $expected_result but got $test_result"
        echo "============================================================"
    fi
    cd ..
done
