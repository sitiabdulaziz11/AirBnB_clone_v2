def do_create(self, args):
        """ Create an object of any class
        """
        ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
        class_name = ''
        name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
        class_match = re.match(name_pattern, args)
        obj_kwargs = {}
        
        # Extract class name
        if class_match is not None:
            class_name = class_match.group('name')
            params_str = args[len(class_name):].strip()
            params = params_str.split(' ')
            str_pattern = r'(?P<typ_str>"([^"]|\")*")'
            float_pattern = r'(?P<typ_float>[-+]?\d+\.\d+)'
            int_pattern = r'(?P<typ_int>[-+]?\d+)'
            param_pattern = '{}=({}|{}|{})'.format(
                name_pattern,
                str_pattern,
                float_pattern,
                int_pattern
            )
            # Parse each parameter
            for param in params:
                param_match = re.fullmatch(param_pattern, param)
                if param_match is not None:
                    key_name = param_match.group('name')
                    str_var = param_match.group('typ_str')
                    float_var = param_match.group('typ_float')
                    int_var = param_match.group('typ_int')
                    
                    # Convert and store the parameter value
                    if float_var is not None:
                        obj_kwargs[key_name] = float(float_var)
                    if int_var is not None:
                        obj_kwargs[key_name] = int(int_var)
                    if str_var is not None:
                        obj_kwargs[key_name] = str_var[1:-1].replace('_', ' ')
            # Ensure 'name' is passed as a parameter
            if 'name' not in obj_kwargs:
                print("** name parameter is missing **")
                return
        else:
            class_name = args
        
        # Error handling for missing class name or invalid class
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        # Create the object and handle database storage
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Set default values for 'id', 'created_at', 'updated_at'
            obj_kwargs['id'] = str(uuid.uuid4())
            obj_kwargs['created_at'] = str(datetime.now())
            obj_kwargs['updated_at'] = str(datetime.now())
            
            new_instance = HBNBCommand.classes[class_name](**obj_kwargs)
            new_instance.save()
            print(new_instance.id)
        else:
            # Create the new instance with the parsed attributes
            new_instance = HBNBCommand.classes[class_name]()
            for key, value in obj_kwargs.items():
                if key not in ignored_attrs:
                    setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)

""" Create an object of any class """
    
    ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
    class_name = ''
    obj_kwargs = {}
    
    # Regular expression to extract class name
    name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
    class_match = re.match(name_pattern, args)
    
    # Extract class name
    if class_match is not None:
        class_name = class_match.group('name')
        params_str = args[len(class_name):].strip()
        params = params_str.split(' ')
        
        # Define patterns to match different data types
        str_pattern = r'(?P<typ_str>"([^"]|\")*")'
        float_pattern = r'(?P<typ_float>[-+]?\d+\.\d+)'
        int_pattern = r'(?P<typ_int>[-+]?\d+)'
        
        # Combine the patterns into a parameter pattern
        param_pattern = '{}=({}|{}|{})'.format(
            name_pattern, str_pattern, float_pattern, int_pattern
        )
        
        # Parse each parameter
        for param in params:
            param_match = re.fullmatch(param_pattern, param)
            if param_match is not None:
                key_name = param_match.group('name')
                str_var = param_match.group('typ_str')
                float_var = param_match.group('typ_float')
                int_var = param_match.group('typ_int')
                
                # Store the parameter value in obj_kwargs
                if float_var is not None:
                    obj_kwargs[key_name] = float(float_var)
                elif int_var is not None:
                    obj_kwargs[key_name] = int(int_var)
                elif str_var is not None:
                    obj_kwargs[key_name] = str_var[1:-1].replace('_', ' ')
        
        # Ensure 'name' is present and not None
        if 'name' not in obj_kwargs or obj_kwargs['name'] == "":
            print("** name parameter is missing or invalid **")
            return
    else:
        print("** class name missing **")
        return
    
    # Error handling for invalid class name
    if class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return
    
    # Create the object and handle database storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # Set default values for 'id', 'created_at', 'updated_at'
        obj_kwargs['id'] = str(uuid.uuid4())
        obj_kwargs['created_at'] = datetime.now()
        obj_kwargs['updated_at'] = datetime.now()
        
        # Create instance with the given attributes
        new_instance = HBNBCommand.classes[class_name](**obj_kwargs)
        new_instance.save()
        print(new_instance.id)
    else:
        # For file storage, create the new instance
        new_instance = HBNBCommand.classes[class_name]()
        for key, value in obj_kwargs.items():
            if key not in ignored_attrs:
                setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)
        
        