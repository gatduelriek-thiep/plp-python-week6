{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4b1e9f59-80eb-47b5-899e-3c9620ce56b1",
   "metadata": {},
   "source": [
    "# Time table file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "26791a94-57ea-4175-a597-aa1b4a54eb9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is your favourite number?  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 Time tables\n",
      "6 Time tables\n",
      "18 Time tables\n",
      "72 Time tables\n",
      "360 Time tables\n",
      "2160 Time tables\n",
      "15120 Time tables\n",
      "120960 Time tables\n",
      "1088640 Time tables\n",
      "10886400 Time tables\n"
     ]
    }
   ],
   "source": [
    "# Ask the user to input his / her favourite number\n",
    "user = int(input(\"What is your favourite number? \"))\n",
    "\n",
    "# Iterate through using a for loop\n",
    "for i in range(1, 11):\n",
    "    user = user * i\n",
    "    print(user,\"Time tables\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14bbdc00-cf06-4888-b833-0b9d406b08e4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
