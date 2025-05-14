import os
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class NumberUnit(str, Enum):
    INTEGER = int
    FLOAT = float


class deleteZeros(str, Enum):
    ZERO_NO = False
    ZERO_YES = True
    
@dataclass
class Numbers:
    number: int | float
    return_unit: NumberUnit
    delete_zeros: deleteZeros
    featureIC:str = "4575"
    success: bool = False
    error_message: Optional[str] = None
    
    def __post_init__(self):
        try:
            # Input data type check for integer
            if not isinstance(self.number, (int, float)):
                raise TypeError("Number must be an integer or float")

            if self.number <= 0:
                raise ValueError("Number must be greater than zero")

            self.defined_unit: NumberUnit = NumberUnit.INTEGER if isinstance(self.number, int) else NumberUnit.FLOAT
            self.success = True
            
        except Exception as e:
            self.error_message = str(e)
    
    @staticmethod
    def __convert_to_int_if_no_decimal(number: float) -> int | float:
        """
        Converts a string to an integer if it represents a whole number, otherwise returns it as a float.
        Args:
            number (float): The number to convert.
        Returns:
            int | float: The converted number, either as an integer or a float.
        """
        float_num = float(number)
        # Проверяем, равно ли число своему целому значению
        if float_num.is_integer():
            return int(float_num)
        return float_num

    def get_result(self) -> int|float:
        """
            Computes and returns a dictionary containing a single key-value pair
            where the key is an integer (1) and the value is a processed number
            based on the specified return unit.
            Returns:
                Dict[int, float]: A dictionary with the processed number as the value.
                    - If `self.return_unit` is `NumberUnit.INTEGER`, the number is
                        converted to an integer.
                    - If `self.return_unit` is `NumberUnit.FLOAT`, the number is
                        converted to a float, incremented by 21.0, and then converted
                        to an integer if it has no decimal part.
                    - Returns an empty dictionary if `self.return_unit` does not
                        match any of the expected units.
            Raises:
                AttributeError: If `self.number` or `self.return_unit` is not defined.
        """
        if self.success:
            print(f"Number: {self.number}, Return Unit: {self.return_unit}")
            if self.return_unit == NumberUnit.INTEGER:
                result = int(self.number)
                return result
            elif self.return_unit == NumberUnit.FLOAT:
                result = float(self.number)
                if self.delete_zeros == deleteZeros.ZERO_NO:
                    result = self.__convert_to_int_if_no_decimal(result)
                else:
                    result = float(result)
                return result
            return 0
        return 0

# Usage example
if __name__ == "__main__":
    
    core:int|float = 5.5
    thread:int = 10
    
    for itm in [core,thread]:
        numb = Numbers(number=itm, 
                        return_unit=NumberUnit.INTEGER, 
                        delete_zeros=deleteZeros.ZERO_NO
                        )
        print(numb.get_result())
    
        """
            Package Die Count -> Number(value, arg1, arg2) -> int без 0
            {
                arg1 = INTEGER
                agr2 = ZERO_NO
            }
            
            
        """
