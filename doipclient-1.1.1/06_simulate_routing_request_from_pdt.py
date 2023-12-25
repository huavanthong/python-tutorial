def serialize (self):
      array = bytearray(self.Length)
      array[0] = self.ProtocolVersion
      array[1] = (~self.ProtocolVersion) & 0xFF
      array[2] = (self.payload.Type >> 8) & 0xFF
      array[3] = (self.payload.Type >> 0) & 0xFF
      array[4] = (self.payload.Length >> 24) & 0xFF
      array[5] = (self.payload.Length >> 16) & 0xFF
      array[6] = (self.payload.Length >> 8) & 0xFF
      array[7] = (self.payload.Length >> 0) & 0xFF
      array[8:len(array)] = self.payload.serialize()
      #Trace array
      print("Message return array: ", array)
      return array

def main():
    paylod


if __name__ == '__main__':
    main()
