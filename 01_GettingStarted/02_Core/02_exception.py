
def external_exception(b):
    if b == 0:
        print("Test run successfully")
        pass
    else: 
        try:
            print("Run internal exception")
            internal_exception(1)
        except Exception as e: 
            print("Catch except from external")
            raise ConnectionError("What is value here", e)
        
def internal_exception(a):
    if a == 0:
        pass
    else: 
        raise ConnectionRefusedError(
                            f"Activation Request failed with code {403}"
                        )


def main():
    # Run test
    external_exception(1)

if __name__ == '__main__':
    main()
