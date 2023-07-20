# DTOgen - Data Transfer Object Generator

DTOgen is a powerful library that allows users to **effortlessly generate Data Transfer Object (DTO) classes** in multiple programming languages from YAML definitions. DTOgen aims to **simplify the process of mapping** JSON or XML data to objects, making it an excellent tool for microservices development.

With DTOgen, syncing Data Transfer Objects (DTOs) across services becomes a seamless process. Since DTOgen allows you to define DTOs in a centralized YAML file and **generates the corresponding classes in multiple programming languages**, you can ensure consistency across your microservices easily. 

DTOgen is designed to handle not only simple data types but also **complex data structures** like lists and maps. With the ability to represent lists and maps in the YAML definitions, DTOgen can generate DTO classes that accurately reflect these data structures in multiple programming languages.

## Features

- Define DTOs in YAML: Users can create their Data Transfer Object definitions in a YAML file, which makes it easy to manage and understand the data structures.

- Multi-language Support: DTOgen supports generating DTO classes for three popular programming languages: Java, Python, and TypeScript. This enables seamless integration into various microservices projects.

- Simple CLI Integration: The library provides a command-line interface (CLI) tool 'dtogen', making it straightforward for users to generate DTO classes for their chosen language.

## Installation

DTOgen can be installed using pip for Python, TypeScript and Java projects.

```bash
pip install dtogen
```

## Usage

1. Create a YAML file with your DTO definitions. For example, `dto_definitions.yaml`:

```yaml
info:
  name: library-dtos
  version: 0.0.1

dtos:
  person :
    attributes :
      - name : name
        type : string
      - name : age
        type : integer
```

2. Run the 'dtogen' CLI command with the desired target language:


```bash
dtogen -i dto_definitions.yaml -o dto_directory -l java --java-package com.example.dtos
```

3. The library will generate the corresponding DTO classes in the specified output directory for the chosen language.

## Example

Given the `dto_definitions.yaml` example above, DTOgen will generate the following DTO classes for each language:

### Java

```java
public class Person {
  public String name;
  public int age;
}
```

### Python

```python
class Person:
  name: str
  age: int
```

### TypeScript

```typescript
export class Person {
    name: string | undefined;
    age: number | undefined;
}
```

DTOgen simplifies the process of creating Data Transfer Objects, enabling developers to focus more on building efficient microservices without worrying about complex data mapping.