# # # # # # # # # # # puts "Hello world" #hi

# # # # # # # # # # =begin
    
# # # # # # # # # # rescue => exception
    
# # # # # # # # # # =end

# # # # # # # # # # # Hello

# # # # # # # # # # myFirstVariable = "I've made a variable"

# # # # # # # # # # puts myFirstVariable

# # # # # # # # # firstNumber = 6
# # # # # # # # # secondNumber = 10

# # # # # # # # # puts firstNumber + secondNumber

# # # # # # # # myFirstString = "My name is Sachin"

# # # # # # # # puts myFirstString.include?("Sac")

# # # # # # # myArray = [5, 3, 5]

# # # # # # # puts myArray.length

# # # # # # # myFirstHash = {
# # # # # # #     "name" => "Sachin"
# # # # # # # }

# # # # # # # puts myFirstHash["name"]

# # # # # # myHash=Hash.new()
# # # # # # myHash[:key] = "value"
# # # # # # puts myHash[:key]

# # # # # isFriend = "true"

# # # # # if isFriend == true
# # # # #     puts "Hello"
# # # # # elsif
# # # # #     puts "Hello 2"
# # # # # else
# # # # #     puts "Goodbye"
# # # # # end

# # # # booleanOne = true
# # # # randomCode = "Hi!"
# # # # if booleanOne
# # # #   puts "I will be printed!"
# # # # elsif randomCode.length>=1
# # # #   puts "Even though the above code is true, I won't be executed because the earlier if statement was true!"
# # # # else
# # # #   puts "I won't be printed because the if statement was executed!"
# # # # end

# # # isFriend = true

# # # unless isFriend
# # #     puts "Hello"
# # # else
# # #     puts "Hello 2"
    
# # # end

# # def sum(a, b)
# #     return a + b
# # end

# # result = sum(2, 3)
# # puts result


# puts 2
# BEGIN {
#     puts 1
# }
# END {
#     puts 0
# }

class Vehicle
    def initialize()
        @noOfWheels = 5
        @horsePower
        @typeOfTank
    end

    def speeding
        puts @noOfWheels
    end

    def driving
        puts "Driving"
    end
end

vehicle = Vehicle.new()

puts vehicle.speeding