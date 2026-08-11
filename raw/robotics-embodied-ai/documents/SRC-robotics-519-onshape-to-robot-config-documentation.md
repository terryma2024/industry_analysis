---
source_id: "SRC-robotics-519"
title: "onshape-to-robot config documentation"
source_type: "technical_documentation"
publisher: "Rhoban"
source_date: "2026-08-10"
url: "https://onshape-to-robot.readthedocs.io/en/latest/config.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-10T15:46:26+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-519
---
# onshape-to-robot config documentation

## Configuration (config.json)

## Specific entries

Below are the global configuration entries. You might also want to check out the following documentation for more specific entries:

- Exporters
- [Processors](https://onshape-to-robot.readthedocs.io/en/latest/processors.html) can define their own specific entries

## config.json entries

Here is an example of complete `config.json` file, with details below:

```javascript
// config.json general options
// for urdf or mujoco specific options, see documentation
{
    // Onshape assembly URL
    "url": "https://cad.onshape.com/documents/11a7f59e37f711d732274fca/w/7807518dc67487ad405722c8/e/5233c6445c575366a6cc0d50",
    // Output format: urdf or mujoco (required)
    "output_format": "urdf",
    // Output filename (default: "robot")
    // Extension (.urdf, .xml) will be added automatically
    "output_filename": "robot",
    // Assets directory (default: "assets")
    "assets_directory": "assets",

    // If you don't use "url", you can alternatively specify the following
    // The Onshape document id to parse, see "getting started" (optional)
    "document_id": "document-id",
    // The document version id (optional)
    "version_id": "version-id",
    // The workspace id (optional)
    "workspace_id": "workspace-id",
    // Element id (optional)
    "element_id": "element-id",
    // Assembly name to use in the document (optional)
    "assembly_name": "robot",

    // Onshape configuration to use (default: "default")
    "configuration": "Configuration=BigFoot;RodLength=50mm",
    // Robot name (default: "onshape")
    "robot_name": "robot",

    // Ignore limits (default: false)
    "ignore_limits": true,

    // Parts to ignore (default: {})
    "ignore": {
        // Ignore visual for visual
        "part1": "visual",
        "screw*": "visual",

        // Ignore everything expect "leg" for collision
        "*" : "collision"
        "!leg": "collision"
    },

    // Whether to keep frame links (default: false)
    "draw_frames": true,
    // Override the color of all links (default: None)
    "color": [0.5, 0.1, 0.1],

    // Disable dynamics retrieval (default: false)
    "no_dynamics": true,

    // Whether to include configuration suffix to part (stl) files (default: true)
    "include_configuration_suffix": false,

    // Post import commands (default: [])
    "post_import_commands" [
        "echo 'Import done'",
        "echo 'Do something else'"
    ],

    // Custom processors
    "processors": [
        "my_project.my_custom_processor:MyCustomProcessor"
    ],

    // Number of decimals to round numerical values (default: 12)
    "round_decimals": 12

    // More options available in specific exporters (URDF, SDF, MuJoCo)
    // More options available in processors
}
```

> [!note] Note
> Since `1.0.0`, all configuration entries are now snake case. For backward compatibility reasons, the old camel case entries are still supported. (for example, `document_id` and `documentId` are equivalent).

### url (required)

The Onshape URL of the assembly to be exported. Be sure you are on the correct tab when copying the URL.

### output\_format (required)

**required**

This should be either `urdf` or `mujoco` to specify which output format is wanted for robot description created by the export.

### output\_filename (default: robot)

This is the name of the output file without extension. By default “robot” (for example: `robot.urdf`, `robot.sdf` or `robot.xml`).

### assets\_directory (default: “assets”)

This is the directory where the assets (like meshes) will be stored.

### assembly\_name (optional)

This can be used to specify the name of the assembly (in the Onshape document) to be used for robot export.

If this is not provided, `onshape-to-robot` will list the assemblies. If more than one assembly is found, an error will be raised.

### document\_id (optional)

If you don’t specify the URL, this is the onshape ID of the document to be imported. It can be found in the Onshape URL, just after `document/`.

```bash
https://cad.onshape.com/documents/XXXXXXXXX/w/YYYYYYYY/e/ZZZZZZZZ
                                  ^^^^^^^^^
                            This is the document id
```

### version\_id (optional)

If you don’t specify the URL, this argument can be used to use a specific version of the document instead of the last one. The version ID can be found in URL, after the `/v/` part when selecting a specific version in the tree.

If it is not specified, the workspace will be retrieved and the live version will be used.

### workspace\_id (optional)

If you don’t specify the URL, this argument can be used to use a specific workspace of the document. This can be used for specific branches ofr your robot without making a version. The workspace ID can be found in URL, after the `/w/` part when selecting a specific version in the tree.

### element\_id (optional)

If you don’t specify the URL, this argument can be used to use a specific element of the document. The element ID can be found in URL, after the `/e/` part when selecting a specific version in the tree.

### configuration (default: “default”)

This is the robot configuration string that will be passed to Onshape. Lists, booleans and quantities are allowed. For example:

[![_images/configuration.png](https://onshape-to-robot.readthedocs.io/en/latest/_images/configuration.png)](https://onshape-to-robot.readthedocs.io/en/latest/_images/configuration.png)

Should be written as the following:

```
Configuration=Long;RemovePart=true;Length=30mm
```

> [!note] Note
> Alternatively, you can specify the configuration as a dictionary:
> 
> ```json
> {
>     // ...
>     "configuration": {
>         "Configuration": "Long",
>         "RemovePart": true,
>         "Length": "30mm"
>     }
> }
> ```

### robot\_name (default: “dirname”)

Specifies the robot name. This value is typically present in the header of the exported files.

If it is not specified, the directory name will be used.

### ignore\_limits (default: false)

If set to `true`, the joint limits coming from Onshape will be ignored during export.

### ignore (default: {})

This can be a list of parts that you want to be ignored during the export.

Alternatively, you can use a dict, where the values are either `all`, `visual` or `collision`. The rules will apply in order of appearance.

You can use wildcards `*` to match multiple parts.

You can prefix the part name with `!` to exclude it from the rule. For example, the following will ignore all parts for visual, except the `leg` part, turning the ignore list to a whitelist:

```json
{
    // Ignore everything from visual
    "*": "collision",
    // Except the leg part
    "!leg": "collision"
}
```

> [!note] Note
> The dynamics of the part will not be ignored, but the visual and collision aspect will.

### draw\_frames (default: false)

When, the part that is used for positionning the frame is by default excluded from the output description (a dummy link is kept instead). Passing this option to `true` will keep it instead.

### no\_dynamics (default: false)

This flag can be set if there is no dynamics. In that case all masses and inertia will be set to 0. In pyBullet, this will result in static object (think of some environment for example).

### color (default: None)

Can override the color for parts (should be an array: `[r, g, b]` with numbers from 0 to 1)

### include\_configuration\_suffix (default: true)

When this flag is set to `true` (default), configurations will be added as a suffix to the part names and STL files.

### post\_import\_commands (default: \[\])

This is an array of commands that will be executed after the import is done. It can be used to be sure that some processing scripts are run everytime you run onshape-to-robot.

### processors (default: None)

See [custom processors](https://onshape-to-robot.readthedocs.io/en/latest/custom_processors.html#custom-processors) for more information.

### round\_decimals (default: 12)

Numbers displayed in export will be rounded up using round() method. The number of decimals that are kept can be controlled using this parameters.
