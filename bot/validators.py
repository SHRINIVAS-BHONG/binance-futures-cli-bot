def validate_inputs(args):
    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT orders require price")

    if args.price is not None and args.price <= 0:
        raise ValueError("Price must be greater than zero")
