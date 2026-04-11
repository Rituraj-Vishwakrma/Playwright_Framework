def retry(func, retries=3):
    # Function to retry execution of another function
    # func → the function we want to execute
    # retries → number of attempts (default = 3)

    for i in range(retries):
        # Loop will run 'retries' times (e.g., 3 times)

        try:
            # Try to execute the function
            return func()
            # If function runs successfully → return result immediately
            # No more retries needed

        except Exception:
            # If function fails (throws error), come here

            if i == retries - 1:
                # Check if this is the LAST attempt
                # retries - 1 because index starts from 0

                raise
                # Raise the exception again if all retries failed
                # This will fail the test