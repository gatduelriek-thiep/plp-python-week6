{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "89c33cc2-f0a0-464e-bf0b-806664820556",
   "metadata": {},
   "source": [
    "# Loop hospital project Python file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "81340803-4396-4d16-bf18-03ad38537551",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# Patient 1\n",
    "for i in range(1, 11): # FIXED: It should stop from 11 since the stopping point is excluded in Python\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9986cf7a-c022-4f49-b5fa-9499b5e08a8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# Patient 2\n",
    "n = 3\n",
    "while n > 0:\n",
    "    print(n) # FIXED: This will create an infinite loop since the stopping point is not specified\n",
    "    n = n - 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d9788aeb-3d89-4d75-a303-101838ea940b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "# Patient 3\n",
    "total = 0\n",
    "for i in range(1, 6):\n",
    "    total = total + i # FIXED: Total variable that is assign to 0 should be put up above the loop\n",
    "print(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6832285-70cf-4a17-a231-3cf7e37da1e7",
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
