class Student:
    def __init__(self, name):
      self.name = name 

      def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

        def raise_hand(self):
         print("Pick me!")
 

      class ChattyStudent(Student):
         def hello(self):
          super().hello()  # Inherited behavior from parent class
         chatty_phrase = (
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! "
            "Oh man, it was so crazy! What, you don't want any spoilers? "
            "Okay well let me just tell you who died..."
        )
         print(chatty_phrase)
         
    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()  # Call the raise_hand() method from the parent class