# Analysis of patches in the Linux Kernel development

## Introduction

automotive contains more and more pcs and embedded systems

autonomouse driving will increase it again

much software \cite{ma:2013:commercial}

can we get an os somewhere?

other industry use more open source

linux is widely used

automotive wants to use it to

certification is missing

-> elisa project

Top-RQ: Can we use linux in safety applications?

-> wie funktioniert die Zertifizierung?

RQ 1: is the development process followed?
RQ 1.1: ignored issues
RQ 1.2: resubmitted patches
RQ 1.3: describe the process of large changes

## certification process

Why is certification so schwer bei automotive?
Welche normen gibt es?
Wie läuft das ab?

Was muss ich alles nachweisen?

### IEC61508-3
#### Inspection
Formal inspection is a structured process to inspect software material that is
carried out by peers of the person producing the material to find defects and to enable the
producer to improve the material. The producer should take no part in the inspection process,
other than to brief the inspectors during the familiarization stage. Formal inspections may be
carried out on specific software elements produced at any phase of the software development
life-cycle.
Prior to the inspection taking place the inspectors should become familiar with the materials
to be inspected. The inspectors’ roles in the inspection process should be clearly defined. An
inspection agenda should be prepared. Entry and exit criteria should be defined based on the
properties required for the software element. Entry criteria are the criteria or requirements
which must be met prior to the inspection taking place. Exit criteria are the criteria or
requirements which must be met to complete a specific process.
During the inspection the findings of the inspection should be formally recorded by the
moderator, whose role is to facilitate the inspection. A consensus on the findings should be
reached by all inspectors. Defects should be classified as either a) requiring rectification prior
to acceptance or b) requiring rectification by a given time / milestone. Defects identified
should be referred to the producer for subsequent rectification after completion of the
inspection. Dependent on the number and scope of identified defects, the moderator may
determine it to be necessary for a further inspection of the software material.

#### Walk-through
Walk-through is an informal technique, carried out by the producer of a
software element in the presence of his peers with the objective of finding defects in the
software element. They may be carried out on specific software elements produced at any
phase of the software development life-cycle.
Specified functions of the safety-related system are examined and evaluated to ensure that
the safety-related system conforms to the requirements given in the specification. Any points
of doubt concerning the implementation and use of the product are documented so they may
be resolved. In contrast with a formal inspection, the author is active during the walkthrough
procedure.
