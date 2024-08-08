def create_template(requirement):
    """
    creates a requirement template
    """
    template = f"""
        You are an expert in identifying nodes
        The list of possible nodes are:
        
        [OnVariableChange]: Triggered when a specified variable changes value.
        [OnKeyRelease]: Triggered when a key is released.
        [OnKeyPress]: Triggered when a key is pressed.
        [OnClick]: Triggered when an element is clicked.
        [OnWindowResize]: Triggered when the window is resized.
        [OnMouseEnter]: Triggered when the mouse pointer enters an element.
        [OnMouseLeave]: Triggered when the mouse pointer leaves an element.
        [OnTimer]: Triggered at specified time intervals.
        [Console]: Prints a message to the console.
        [Alert]: Displays an alert message.
        [Log]: Logs information for debugging purposes.
        [Assign]: Assigns a value to a variable.
        [SendRequest]: Sends a network request.
        [Navigate]: Navigates to a different URL or page.
        [Save]: Saves data to local storage or a database.
        [Delete]: Deletes specified data or records.
        [PlaySound]: Plays an audio file.
        [PauseSound]: Pauses an audio file.
        [StopSound]: Stops an audio file.
        [Branch]: Conditional node that branches based on a true/false evaluation.
        [Map]: Transforms data from one format to another.
        [Filter]: Filters data based on specified criteria.
        [Delay]: Delays a given action
        [Reduce]: Reduces a list of items to a single value.
        [Sort]: Sorts data based on specified criteria.
        [GroupBy]: Groups data by a specified attribute.
        [Merge]: Merges multiple datasets into one.
        [Split]: Splits data into multiple parts based on criteria
        [Show]: Displays information on the screen.
        [Hide]: Hides information from the screen.
        [Update]: Updates the display with new information.
        [DisplayModal]: Displays a modal dialog.
        [CloseModal]: Closes an open modal dialog.
        [Highlight]: Highlights an element on the screen.
        [Tooltip]: Shows a tooltip with additional information.
        [RenderChart]: Renders a chart with specified data.
        [FetchData]: Fetches data from an API or database.
        [StoreData]: Stores data in a variable or storage.
        [UpdateData]: Updates existing data.
        [DeleteData]: Deletes specified data.
        [CacheData]: Caches data for performance improvement.
    
        Given a requirement identify the relevant nodes. You will follow the examples below to build your response.
        Example 1:
        Prompt: Navigate to a new page after a delay of 3 seconds when the user clicks a button.
        Sequence of Nodes:
        1. [OnClick]
        2. [Delay]
        3. [Navigate]
    
        Example 2:
        Prompt: Fetch user data and display it in a modal when a button is clicked.
        Sequence of Nodes:
        1. [OnClick]
        2. [FetchData]
        3. [DisplayModal]
        
        Example 3:
        Prompt: Reduce a list of scores to find the highest score and log the result.
        Sequence of Nodes:
        1. [Reduce]
        2. [Log]
        
        Example 4:
        Prompt: Cache fetched data to improve performance and display the data on the screen.
        Sequence of Nodes:
        1. [FetchData]
        2. [CacheData]
        3. [Show]
        
        Example 5:
        Prompt: Log a message when a key is pressed and display the key value on the screen.
        Sequence of Nodes:
        1. [OnKeyPress]
        2. [Log]
        3. [Show]
        
        Example 6:
        Prompt: Highlight an element when the mouse enters it and remove the highlight when the mouse leaves.
        Sequence of Nodes:
        1. [OnMouseEnter]
        2. [Highlight]
        3. [OnMouseLeave]
        
        Example 7:
        Prompt: Filter out items that are out of stock and sort the remaining items by price before displaying them on the screen.
        Sequence of Nodes:
        1. [Filter]
        2. [Sort]
        3. [Show]

    
        Now, based on the above mentioned examples, identify the sequence of nodes. Dont include the examples or explanation in your response
    
        Prompt: {requirement}
        Sequence of Nodes:
        """

    return template