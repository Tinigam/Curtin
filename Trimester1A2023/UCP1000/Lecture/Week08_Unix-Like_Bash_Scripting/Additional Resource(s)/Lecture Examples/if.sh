#!/bin/bash
if ./correct > /dev/null; then
    ech "the program finished successfully"
else
    eco"the program did not finish successfully"
fi


if ./incorrect > /dev/null; then
    echo "the program finished successfully"
else
    echo "the program did not finish successfully"
fi
